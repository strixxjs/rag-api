from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue

class VectorStore:
    def __init__(self, client: QdrantClient, collection_name: str):
        self.client = client
        self.collection_name = collection_name


    def ensure_collection_exists(self) -> None:
        if not self.client.collection_exists(self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=384, distance=Distance.COSINE)
            )


    def upsert_chunks(self, chunks: list[dict]):
        points = list()
        for chunk in chunks:
            point = PointStruct(id=chunk["id"], vector=chunk["vector"], payload={
                "text": chunk["text"],
                "filename": chunk["filename"],
                "source": chunk["source"],
                "document_id": chunk["document_id"],
            })
            points.append(point)
        self.client.upsert(collection_name=self.collection_name, points=points)


    def search(self, query_vector: list[float], top_k: int = 5) -> list[dict]:
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=top_k,
            with_payload=True
        )
        found = []
        for result in results:
            found.append({
                "text": result.payload["text"],
                "filename": result.payload["filename"],
                "source": result.payload["source"],
                "document_id": result.payload["document_id"],
                "score": result.score
            })
        return found

    def delete_document(self, document_id: str) -> None:
        self.client.delete(
            collection_name=self.collection_name,
            points_selector=Filter(
                must=[
                    FieldCondition(
                        key="document_id",
                        match=MatchValue(value=document_id)
                    )
                ]
            )
        )