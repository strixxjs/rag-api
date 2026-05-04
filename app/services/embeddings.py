from sentence_transformers import SentenceTransformer


class EmbeddingsService:
    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)

    def embed(self, text: str) -> list[float]:
        vector = self.model.encode(text)
        return vector.tolist()
