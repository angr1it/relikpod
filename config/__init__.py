from typing import Optional

from pydantic_settings import BaseSettings
import spacy


class AppSettings(BaseSettings):
    relik_model: Optional[str] = "relik-ie/relik-relation-extraction-small"

    openai_llm_model: Optional[str] = "gpt-4o-mini"
    openai_api_key: str
    openai_llm_temperature: Optional[float] = 0.0
    openai_embedding_model: Optional[str] = "text-embedding-3-small"

    class Config:
        env_file: str = ".env"
        extra = "allow"


app_settings = AppSettings()
coref_nlp = spacy.load("en_core_web_lg")
coref_nlp.add_pipe("coreferee")
