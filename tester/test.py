import json
import sys
from json import JSONDecodeError

from llama_index.llms.ollama import Ollama
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.response_synthesizers import ResponseMode
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core import ChatPromptTemplate
from llama_index.core import Settings
from chatbot.txt_retriever import TxtRetriever
from chatbot.config import Config
from test_cases import tests

collection = 'Dementia'
prompt = '1'


def test(model: str, temperature: float):
    Settings.llm = Ollama(model=model, temperature=temperature)

    vector_retriever_chunk = TxtRetriever(collection)

    text_template = ChatPromptTemplate([
        ChatMessage(
            role=MessageRole.SYSTEM,
            content='\n'.join(Config.get('prompts.diagnosis.system')),
        ),
        ChatMessage(
            role=MessageRole.USER,
            content='\n'.join(Config.get('prompts.diagnosis.user')),
        ),
    ])

    query_engine = RetrieverQueryEngine.from_args(
        vector_retriever_chunk,
        verbose=True,
        response_mode=ResponseMode.COMPACT,
        text_qa_template=text_template)

    for test in tests:
        response = query_engine.query(test['prompt'])
        diagnosis = response.response
        if not diagnosis.endswith('}'):
            diagnosis = diagnosis + '}'
        try:
            extract = json.loads(diagnosis)
            print(';'.join([model, prompt, str(temperature), test['id'],
                            str(extract['Number']),
                            test['expected'], test['prompt'],
                            extract['Explanation']]))
        except JSONDecodeError:
            print('error parsing json', file=sys.stderr)
            print(response.response, file=sys.stderr)


print(';'.join(['model', 'prompt', 'temperature', 'test id', 'symptoms detected',
                'symptoms expected', 'input',
                'explanation']))

for cur_model in [
        #'mistral',
        'llama2'
    ]:
    for cur_temperature in [0.75, 0.60, 0.45, 0.30, 0.15, 0]:
        test(cur_model, cur_temperature)
