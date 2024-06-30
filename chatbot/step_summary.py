"""
LLM RAG Chatbot
"""
from chatbot.execution_context import ExecutionContext
from chatbot.steps import Step, Prompts


class SummaryPrompts(Prompts):
    """
    The SummaryPrompts class represents a set of prompt templates for
    generating the summaries of the dialogues.
    """

    def __init__(self):
        """
        Creates the instance using the prompts.summary configuration.
        """
        super().__init__('prompts.summary')


class SummaryGenerationStep(Step):
    """
    The SummaryGenerationStep class represents the step to generate
    the summaries of the dialogues.
    """
    def __init__(self, execution_context: ExecutionContext):
        super().__init__(prompts=SummaryPrompts(), execution_context=execution_context)
