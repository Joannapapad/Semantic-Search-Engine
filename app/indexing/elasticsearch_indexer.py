from elasticsearch import Elasticsearch
from app.utils.loaders import load_documents

es = Elasticsearch("http://localhost:9200")

INDEX_NAME = "documents"

document_ids, document_texts = load_documents("data/documents.csv")

for doc_id, text in zip(document_ids, document_texts):

    document = {
        "text": text
    }

    es.index(
        index=INDEX_NAME,
        id=int(doc_id),
        document=document
    )

print("ElasticSearch indexing complete")