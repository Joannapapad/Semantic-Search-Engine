from sentence_transformers import SentenceTransformer
from app.utils.config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)