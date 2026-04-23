from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, HttpUrl


class DocumentType(str, Enum):
    PDF = "pdf"
    DOCX = "docx"
    TXT = "txt"
    URL = "url"
    GOOGLE_DOC = "google-doc"


class DocumentMetadata(BaseModel):
    document_id: UUID
    filename: str
    document_type: DocumentType
    source: str
    total_chunks: int
    created_at: datetime


class DocumentUploadResponse(BaseModel):
    document_id: UUID
    filename: str
    document_type: DocumentType
    total_chunks: int
    message: str = "Document Upload Successful"


class DocumentListResponse(BaseModel):
    documents: list[DocumentMetadata]
    total: int


class DeleteDocumentResponse(BaseModel):
    document_id: UUID
    message: str


class URLUploadRequest(BaseModel):
    url: HttpUrl
    title: str | None = None
