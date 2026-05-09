from fastapi import APIRouter

from app.retrieval.semantic_search import semantic_search
from app.retrieval.bm25_search import bm25_search
from app.retrieval.hybrid_search import hybrid_search

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/search")
def bm25(query: str, k: int = 20):
    return bm25_search(query, k)

@router.get("/semantic-search")
def semantic(query: str, k: int = 20):
    return semantic_search(query, k)

@router.get("/hybrid-search")
def hybrid_search_endpoint(query: str, k: int = 10):

    return hybrid_search(query, k)