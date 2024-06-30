"""
LLM RAG Chatbot
"""
from typing import List
from llama_index import QueryBundle
from llama_index.core.base_retriever import BaseRetriever
from llama_index.schema import NodeWithScore, Document
from pathlib import Path


class TxtRetriever(BaseRetriever):
    """
     NullRetriever is a simple retriever that returns an empty result.

     It implements the BaseRetriever interface but always returns a single
     NodeWithScore containing an empty Document. This acts as a placeholder
     retriever that can be used during development or when no primary
     retriever is available/functional. By consistently returning an empty
     result, it prevents errors from occurring downstream.
     """

    def __init__(self, collection: str):
        super().__init__()
        self._collection = collection

    def _retrieve(self, query_bundle: QueryBundle) -> List[NodeWithScore]:
        """
        It returns an empty list of nodes with scores.
        :param query_bundle: query.
        :return: an empty list of NodeWithScore.
        """
        filename = f"kb/diagnosis/{self._collection}.txt"
        contents = Path(filename).read_text()
        node = Document(text=contents, node_id=self._collection, metadata={'file_name': filename})
        return [NodeWithScore(node=node, score=1)]
