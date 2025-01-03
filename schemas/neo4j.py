from pydantic import BaseModel


class Neo4jConfig(BaseModel):
    username: str
    password: str
    url: str
