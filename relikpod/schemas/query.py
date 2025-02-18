from typing import Optional

from pydantic import BaseModel

from relikpod.schemas.neo4j import Neo4jConfig


class RelikpodQueryRequest(BaseModel):
    neo4j: Neo4jConfig
    queries: list[str]


class RelikpodQueryResponse(BaseModel):
    results: list[dict]
    message: Optional[str] = "Query executed successfully."
