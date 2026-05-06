from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

# Load dataset
DOCUMENTS_PATH = "../data/documents.csv"

documents_df = pd.read_csv(DOCUMENTS_PATH)

documents_text = documents_df["text"].tolist()

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
embeddings = model.encode(documents_text, convert_to_numpy=True)

# Save embeddings
np.save("document_embeddings.npy", embeddings)

print(f"Generated embeddings for {len(documents_text)} documents.")