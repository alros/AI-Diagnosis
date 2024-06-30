"""
LLM RAG Chatbot
"""
from execution_context import ExecutionContext
from step_chat_generation import ChatGenerationStep
from step_diagnosis import DiagnosisGenerationStep
from step_final_diagnosis import FinalDiagnosisGenerationStep
from step_summary import SummaryGenerationStep
from page import Page

#
# This is the main script to run the LLM RAG Chatbot.
#

if __name__ == "__main__":
    # assemble the dependencies
    execution_context = ExecutionContext()
    step_chat = ChatGenerationStep(execution_context=execution_context)
    step_summary = SummaryGenerationStep(execution_context=execution_context)
    step_diagnosis = DiagnosisGenerationStep(execution_context=execution_context)
    step_final_diagnosis = FinalDiagnosisGenerationStep(execution_context=execution_context)

    # wire the dependencies into the streamlit Page
    Page(step_chat=step_chat,
         step_summary=step_summary,
         step_diagnosis=step_diagnosis,
         step_final_diagnosis=step_final_diagnosis)
