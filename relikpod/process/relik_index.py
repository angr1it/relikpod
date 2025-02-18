from relikpod.handlers.relik import index_documents
from relikpod.schemas.index import RelikpodIndexRequest, RelikpodIndexResponse
from relikpod.index import get_index


def process_index_request(request: dict) -> dict:
    try:
        request_model = RelikpodIndexRequest(**request)
    except Exception as e:
        return RelikpodIndexResponse(success=False, message=str(e))

    index = get_index(neo4j_config=request_model.neo4j)
    index_documents(index=index, documents=request_model.documents)

    return RelikpodIndexResponse(
        success=True,
        message=f"Indexed {len(request_model.documents)} documents.",
    ).model_dump()
