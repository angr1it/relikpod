from llama_index.extractors.relik.base import RelikPathExtractor

from relikpod.config import app_settings


relik = RelikPathExtractor(
    model=app_settings.relik_model,
    model_config={"skip_metadata": True},
)
