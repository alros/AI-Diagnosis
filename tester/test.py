import datetime
import json
import sys
from json import JSONDecodeError
from typing import List

from httpx import RemoteProtocolError, ReadTimeout
from llama_index.llms.ollama import Ollama
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.response_synthesizers import ResponseMode
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core import ChatPromptTemplate
from llama_index.core import Settings
from chatbot.txt_retriever import TxtRetriever
from test_cases import tests
from prompts import prompts

MAX_RETRIES = 2

collections = ['Dementia', 'Alzheimer']
log_file = open(f'logfile-{datetime.datetime.now()}.csv', 'w')


def log_print(log: str):
    print(log)
    log_file.write(log + '\n')


def test(model: str, temperature: float, system_prompt: str, user_prompt: str, collection: str):
    Settings.llm = Ollama(model=model, temperature=temperature)

    vector_retriever_chunk = TxtRetriever(collection)

    text_template = ChatPromptTemplate([
        ChatMessage(
            role=MessageRole.SYSTEM,
            content=system_prompt,
        ),
        ChatMessage(
            role=MessageRole.USER,
            content=user_prompt,
        ),
    ])

    query_engine = RetrieverQueryEngine.from_args(
        vector_retriever_chunk,
        verbose=True,
        response_mode=ResponseMode.COMPACT,
        text_qa_template=text_template)

    for test in tests:
        hack = False
        retries = 0
        done = False
        while retries < MAX_RETRIES and not done:
            retries += 1
            try:
                response = query_engine.query(test['prompt'])
                diagnosis = response.response

                if diagnosis.find("```json") == 0:
                    diagnosis = diagnosis[len("```json\n"):-4]
                    hack = True
                if diagnosis.find('“') >= 0 or diagnosis.find('”') >= 0:
                    diagnosis = diagnosis.replace('“', '"').replace('”', '"')
                    hack = True
                if not diagnosis.endswith('}'):
                    idx = diagnosis.find('}')
                    if idx >= 0:
                        diagnosis = diagnosis[0:idx + 1]
                    else:
                        diagnosis = diagnosis + '}'
                    hack = True

                extract = json.loads(diagnosis)
                if 'Explanation' not in extract:
                    raise JSONDecodeError
                explanation = ' '.join(extract['Explanation']) if isinstance(extract['Explanation'], List) else extract[
                    'Explanation']
                hack = hack or isinstance(extract['Explanation'], List)

                log_print(';'.join([model, collection, str(prompt), str(temperature), test['id'], 'true', str(hack),
                                    str(extract['Number']),
                                    test['expected'], test['prompt'],
                                    explanation]))
                done = True
            except (JSONDecodeError, RemoteProtocolError, TypeError) as _:
                print('error parsing json', file=sys.stderr)
                print(response.response, file=sys.stderr)
                if retries == MAX_RETRIES:
                    log_print(
                        ';'.join([model, collection, str(prompt), str(temperature), test['id'], 'false', str(hack),
                                  '',
                                  test['expected'], test['prompt'],
                                  '']))
            except (ReadTimeout) as _:
                print('timeout', file=sys.stderr)
                if retries == MAX_RETRIES:
                    log_print(
                        ';'.join([model, collection, str(prompt), str(temperature), test['id'], 'false', str(hack),
                                  '',
                                  test['expected'], test['prompt'],
                                  '']))


log_print(';'.join(['model', 'rag file', 'prompt', 'temperature', 'test id', 'successful', 'hack', 'symptoms detected',
                    'symptoms expected', 'input',
                    'explanation']))

for collection in collections:
    for prompt in range(1, 8):
        system_prompt = '\n'.join(prompts[prompt - 1]['system'])
        user_prompt = '\n'.join(prompts[prompt - 1]['user'])

        for cur_model in [  # 'orca2',
            # 'orca-mini',
            # 'gemma2',
            # 'phi3'
            # 'llama2:13b',

            'mistral:7b-text-q8_0',
            'mistral:7b-instruct-q8_0',
            'mistral',
            'llama2',
            'llama3'
            'mistral:instruct'
        ]:
            for cur_temperature in [1, 0.9, 0.75, 0.60, 0.45, 0.30, 0.15, 0]:
                test(cur_model, cur_temperature, system_prompt, user_prompt, collection)

log_file.close()
