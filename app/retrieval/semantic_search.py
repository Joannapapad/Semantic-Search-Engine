import faiss
import numpy as np

from app.embeddings.embedding_model import model
from app.utils.loaders import load_documents
from app.utils.config import *

index = faiss.read_index(FAISS_INDEX_PATH)

document_ids, document_texts = load_documents(DOCUMENTS_PATH)

doc_lookup = {
    doc_id: text
    for doc_id, text in zip(document_ids, document_texts)
}

def semantic_search(query, k=20):

    query_vector = model.encode(
        [query],
        convert_to_numpy=True
    )

    faiss.normalize_L2(query_vector)

    scores, ids = index.search(query_vector, k)

    results = []

    for score, doc_id in zip(scores[0], ids[0]):

        results.append({
            "doc_id": int(doc_id),
            "score": float(score),
            "text": doc_lookup[int(doc_id)][:300]
        })

    return results