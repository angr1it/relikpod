from llama_index.core import Document

from relikpod.index.graph import CustomPropertyGraphIndex


def index_documents(
    index: CustomPropertyGraphIndex, documents: list[Document]
):
    """
    Индексирует список документов в базе данных графов Neo4j.

    Args:
        index (CustomPropertyGraphIndex): Индекс графа свойств.
        documents (list[Document]): Список документов для индексации в базе
        данных.
    """
    for doc in documents:
        index.update_ref_doc(document=doc)


def query(index: CustomPropertyGraphIndex, query: str):
    """
    Выполняет запрос в базе данных графов Neo4j.

    Args:
        index (CustomPropertyGraphIndex): Индекс графа свойств.
        query (str): Запрос для выполнения.

    Returns:
        list[dict]: Результаты запроса.
    """
    engine = index.as_query_engine(include_text=True)

    return engine.query(query)
