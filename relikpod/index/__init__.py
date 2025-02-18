from relikpod.config.llm import llm, embed_model
from relikpod.config.relik import relik
from relikpod.index.graph import CustomPropertyGraphIndex
from relikpod.config.graph import init_neo4j
from relikpod.schemas.neo4j import Neo4jConfig


def get_index(neo4j_config: Neo4jConfig):
    neo4j = init_neo4j(neo4j_config)
    return CustomPropertyGraphIndex(
        kg_extractors=[relik],
        property_graph_store=neo4j,
        llm=llm,
        embed_model=embed_model,
    )
