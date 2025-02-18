from typing import Type, Any, Sequence

from llama_index.core import Document, PropertyGraphIndex


class CustomPropertyGraphIndex(PropertyGraphIndex):
    @classmethod
    def from_documents(
        cls: Type["CustomPropertyGraphIndex"],
        documents: Sequence[Document],
        **kwargs: Any,
    ) -> "CustomPropertyGraphIndex":
        """Create index from documents, with pre-cleanup in graph_store."""

        doc_ids = [document.doc_id for document in documents]

        graph_store = kwargs.get("property_graph_store")
        if graph_store:
            graph_store.delete_llama_nodes(ref_doc_ids=doc_ids)

        return super().from_documents(
            documents=documents,
            **kwargs,
        )
