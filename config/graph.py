from llama_index.graph_stores.neo4j import Neo4jPGStore


def init_neo4j(username: str, password: str, url: str):
    """
    Initializes a connection to a Neo4j graph database.

    Args:
        username (str): The username for the Neo4j database.
        password (str): The password for the Neo4j database.
        url (str): The URL of the Neo4j database.

    Returns:
        Neo4jPGStore: An instance of Neo4jPGStore connected to the specified
        database.
    """
    return Neo4jPGStore(
        username=username, password=password, url=url, refresh_schema=False
    )
