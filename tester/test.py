from llama_index.llms.ollama import Ollama
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.response_synthesizers import ResponseMode
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core import ChatPromptTemplate
from llama_index.core import Settings
from chatbot.txt_retriever import TxtRetriever
from chatbot.config import Config

model = 'mistral'
collection = 'Dementia'

Settings.llm = Ollama(model=model)

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

prompt = 'The 75-year-old patient is experiencing age-related cognitive decline, particularly in recognizing people and following complex conversations, as well as occasional memory lapses and disorientation.'

response = query_engine.query(prompt)

print(response.response)