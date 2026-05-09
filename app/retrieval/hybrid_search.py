from app.retrieval.bm25_search import bm25_search
from app.retrieval.semantic_search import semantic_search

def hybrid_search(query, k=20):

    bm25_results = bm25_search(query, k=50)

    semantic_results = semantic_search(query, k=50)

    combined_scores = {}

    for rank, result in enumerate(bm25_results):

        doc_id = str(result["doc_id"])

        combined_scores[doc_id] = combined_scores.get(doc_id, 0)

        combined_scores[doc_id] += 1 / (rank + 1)

    for rank, result in enumerate(semantic_results):

        doc_id = str(result["doc_id"])

        combined_scores[doc_id] = combined_scores.get(doc_id, 0)

        combined_scores[doc_id] += 1 / (rank + 1)

    ranked = sorted(
        combined_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:k]