from collections import defaultdict

from app.retrieval.bm25_search import bm25_search
from app.retrieval.semantic_search import semantic_search


def hybrid_search(query, k=10, rrf_k=60):
    """
    Hybrid retrieval using Reciprocal Rank Fusion (RRF).

    Combines:
    - BM25 lexical retrieval
    - Semantic vector retrieval

    Args:
        query (str): user query
        k (int): number of final results
        rrf_k (int): RRF smoothing constant

    Returns:
        list: ranked hybrid results
    """

    # Retrieve larger candidate sets
    bm25_results = bm25_search(query, k=50)
    semantic_results = semantic_search(query, k=50)

    # Store fused scores
    fused_scores = defaultdict(float)

    # Store document metadata
    doc_lookup = {}

    # -----------------------------
    # BM25 contribution
    # -----------------------------
    for rank, result in enumerate(bm25_results):

        doc_id = result["doc_id"]

        # Reciprocal Rank Fusion score
        fused_scores[doc_id] += 1 / (rrf_k + rank + 1)

        doc_lookup[doc_id] = result

    # -----------------------------
    # Semantic contribution
    # -----------------------------
    for rank, result in enumerate(semantic_results):

        doc_id = result["doc_id"]

        fused_scores[doc_id] += 1 / (rrf_k + rank + 1)

        # Keep document metadata
        if doc_id not in doc_lookup:
            doc_lookup[doc_id] = result

    # -----------------------------
    # Sort by fused score
    # -----------------------------
    ranked_docs = sorted(
        fused_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # -----------------------------
    # Build final results
    # -----------------------------
    final_results = []

    for doc_id, hybrid_score in ranked_docs[:k]:

        result = {
            "doc_id": doc_id,
            "hybrid_score": round(hybrid_score, 6),
            "text": doc_lookup[doc_id]["text"]
        }

        final_results.append(result)

    return final_results