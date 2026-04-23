from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title="RAG API",
    description="Retrieval-Augmented Generation API with source citations",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    return {"status": "ok", "collection": settings.qdrant_collection_name}