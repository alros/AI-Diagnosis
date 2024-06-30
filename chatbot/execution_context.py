"""
LLM RAG Chatbot
"""
import os
from llama_index.core import Settings
from llama_index.core.callbacks import LlamaDebugHandler, CallbackManager, CBEventType
from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.llms.llama_cpp.llama_utils import (
    messages_to_prompt,
    completion_to_prompt,
)
from chatbot.config import Config


class ExecutionContext:
    """
    The ExecutionContext class represents the shared execution context
    passed between steps in the conversational workflow.

    It acts as a wrapper of ServiceContext, initialises the LLM with the
    model specified in `config.yaml`, and handles LLM's response for
    logging.
    """

    def __init__(self):
        """
        Initializes the execution context and sets the model.
        """
        self._llm = LlamaCPP(
            # You can pass in the URL to a GGML model to download it automatically
            model_url=None,
            # optionally, you can set the path to a pre-downloaded model instead of model_url
            model_path=os.environ['MODEL_PATH'],
            temperature=0.1,
            max_new_tokens=1000,
            # llama2 has a context window of 4096 tokens, but we set it lower to allow for some wiggle room
            context_window=3900,
            # kwargs to pass to __call__()
            generate_kwargs={},
            # kwargs to pass to __init__()
            # set to at least 1 to use GPU
            model_kwargs={"n_gpu_layers": 1},
            verbose=True,
        )



        self._service_context = None
        self._llama_debug = None
        self._llama_debug = LlamaDebugHandler(print_trace_on_end=True)
        callback_manager = CallbackManager([self._llama_debug])
        Settings.llm = self._llm
        Settings.callback_manager = callback_manager

    def handle(self, response) -> None:
        """
        Method that post processes the response from the LLM. It is used
        for logging.

        :param response: response from the LLM/Ollama.
        :return: None
        """
        self._print_debug(response=response)

    def _print_debug(self, response) -> None:
        """
        Prints debug information from the response.

        :param llama_debug: instance of LlamaDebugHandler linked in the context.
        :param response: LLM's response to process.
        :return: None
        """

        event_pairs = self._llama_debug.get_event_pairs(CBEventType.LLM)
        # print('\n==================== RESPONSE ====================\n')
        # print('\n  ------------------ source nodes ----------------')
        # for node in response.source_nodes:
        #     print(f'  {node.node_id}: score {node.score} - {node.node.metadata["file_name"]}\n{node.text}\n\n')
        # print('  ----------------- /source nodes ----------------\n')
        # print('\n  ------------------ events pairs ----------------\n')
        # for event_pair in event_pairs:
        #     print(f'  {event_pair[0]}')
        #     print(f'  {event_pair[1].payload.keys()}')
        #     print(f'  {event_pair[1].payload["response"]}')
        # print('  ------------------ events pairs ----------------\n')
        # print('\n=================== /RESPONSE ====================\n')
