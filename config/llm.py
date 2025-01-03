import os

from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI

from relikpod.config import app_settings


os.environ["OPENAI_API_KEY"] = app_settings.openai_api_key

llm = OpenAI(
    model=app_settings.openai_llm_model,
    temperature=app_settings.openai_llm_temperature
)
embed_model = OpenAIEmbedding(model_name=app_settings.openai_embedding_model)
