from elasticsearch import Elasticsearch
import pandas as pd

# Initialize ElasticSearch client
es_client = Elasticsearch("http://localhost:9200")

# Index configuration
INDEX_NAME = "documents_index"

# Load dataset
DOCUMENTS_PATH = "../data/documents.csv"

documents_df = pd.read_csv(DOCUMENTS_PATH)

# Create index mapping
mapping = {
    "mappings": {
        "properties": {
            "doc_id": {"type": "keyword"},
            "text": {"type": "text"}
        }
    }
}

# Delete old index if it exists
if es_client.indices.exists(index=INDEX_NAME):
    es_client.indices.delete(index=INDEX_NAME)

# Create index
es_client.indices.create(index=INDEX_NAME, body=mapping)

# Insert documents into ElasticSearch
for _, row in documents_df.iterrows():
    document = {
        "doc_id": str(row["doc_id"]),
        "text": row["text"]
    }

    es_client.index(index=INDEX_NAME, document=document)

print(f"Indexed {len(documents_df)} documents successfully.")