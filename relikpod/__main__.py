import runpod

from relikpod.process.relik_index import process_index_request
from relikpod.process.relik_query import process_query_request

runpod.serverless.start(
    {
        "relik_index": process_index_request,
        "relik_query": process_query_request
    }
)
