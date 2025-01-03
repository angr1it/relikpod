from pydantic import BaseModel

from relikpod.schemas.neo4j import Neo4jConfig


class Document(BaseModel):
    document_id: str
    text: str


class RelikpodIndexRequest(BaseModel):
    neo4j: Neo4jConfig
    documents: list[Document]


class RelikpodIndexResponse(BaseModel):
    success: bool
    message: str
