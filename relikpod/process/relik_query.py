from relikpod.handlers.relik import query
from relikpod.schemas.query import RelikpodQueryRequest, RelikpodQueryResponse
from relikpod.index import get_index
from relikpod.config.logger import get_logger


logger = get_logger(__name__)


def process_query_request(request: dict) -> dict:
    try:
        request_model = RelikpodQueryRequest(**request)
    except Exception as e:
        return RelikpodQueryResponse(results=[], message=str(e))

    index = get_index(neo4j_config=request_model.neo4j)

    results = []
    for q in request_model.queries:
        results.append(query(index=index, query=q))

    logger.info(f"Query results: {results}")
    return RelikpodQueryResponse(
        results=results,
    ).model_dump()
