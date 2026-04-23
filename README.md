# RAG API

REST API for Retrieval-Augmented Generation with source citations.

## Tech Stack
- **FastAPI** — REST API
- **Qdrant** — vector database
- **Groq (LLaMA 3.3 70b)** — LLM
- **sentence-transformers** — local embeddings (all-MiniLM-L6-v2)

## API Contract
Full OpenAPI spec available at `/docs` (Swagger) or `/openapi.json`

## Quick Start

```bash
# 1. Clone & setup
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"

# 2. Environment
cp .env.example .env
# Fill in GROQ_API_KEY in .env

# 3. Start Qdrant
docker compose up -d

# 4. Start API
uvicorn app.main:app --reload
```

## Endpoints Overview
| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| POST | `/api/v1/documents/upload` | Upload document |
| GET | `/api/v1/documents/` | List documents |
| DELETE | `/api/v1/documents/{id}` | Delete document |
| POST | `/api/v1/query/` | Query with sources |

## For TypeScript/Go developers
Branch this repo and rewrite using `/openapi.json` as the contract.
The API behavior must stay identical — same request/response schemas.