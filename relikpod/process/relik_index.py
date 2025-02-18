from relikpod.handlers.relik import index_documents
from relikpod.schemas.index import RelikpodIndexRequest, RelikpodIndexResponse
from relikpod.index import get_index


def process_index_request(request: dict) -> dict:
    try:
        request_model = RelikpodIndexRequest(**request)
    except Exception as e:
        return RelikpodIndexResponse(success=False, message=str(e))

    return process_index_query(request_model).model_dump()


def process_index_query(request: RelikpodIndexRequest) -> RelikpodIndexResponse:
    index = get_index(neo4j_config=request.neo4j)
    index_documents(index=index, documents=request.documents)

    return RelikpodIndexResponse(
        success=True,
        message=f"Indexed {len(request.documents)} documents.",
    )
