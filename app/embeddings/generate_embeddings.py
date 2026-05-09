import numpy as np
import faiss

from app.embeddings.embedding_model import model
from app.utils.loaders import load_documents
from app.utils.config import *

document_ids, document_texts = load_documents(DOCUMENTS_PATH)

embeddings = model.encode(
    document_texts,
    batch_size=256,
    show_progress_bar=True,
    convert_to_numpy=True
)

faiss.normalize_L2(embeddings)

np.save(EMBEDDINGS_PATH, embeddings)

print("Embeddings shape:", embeddings.shape)