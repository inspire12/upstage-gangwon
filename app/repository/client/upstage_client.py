from typing import List
from openai import OpenAI
from app.core.settings import upstage_settings


class UpstageClient:

    def __init__(self):
        self.client = OpenAI(api_key=upstage_settings.api_key, base_url=upstage_settings.base_url)

    def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        try:
            response = self.client.embeddings.create(
                model=upstage_settings.embedding_model,
                input=texts
            )
            return [embedding.embedding for embedding in response.data]
        except Exception as e:
            raise RuntimeError(f"Failed to create embeddings: {str(e)}")

    def create_embedding(self, text: str) -> List[float]:
        return self.create_embeddings([text])[0]