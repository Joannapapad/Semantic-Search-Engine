import faiss
import numpy as np

from app.utils.loaders import load_documents
from app.utils.config import *

document_ids, _ = load_documents(DOCUMENTS_PATH)

embeddings = np.load(EMBEDDINGS_PATH)

dimension = embeddings.shape[1]

index = faiss.IndexIDMap(
    faiss.IndexFlatIP(dimension)
)

index.add_with_ids(
    embeddings,
    np.array(document_ids)
)

faiss.write_index(index, FAISS_INDEX_PATH)

print("FAISS index created")
print("Total vectors:", index.ntotal)