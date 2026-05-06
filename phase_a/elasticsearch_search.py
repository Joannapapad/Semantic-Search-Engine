from elasticsearch import Elasticsearch

# Initialize ElasticSearch client
es_client = Elasticsearch("http://localhost:9200")

INDEX_NAME = "documents_index"


def run_search(query, top_k=5):
    """
    Execute BM25 retrieval using ElasticSearch.
    """

    search_body = {
        "query": {
            "match": {
                "text": query
            }
        },
        "size": top_k
    }

    response = es_client.search(index=INDEX_NAME, body=search_body)

    return response["hits"]["hits"]


# Example query
query = "machine learning algorithms"
results = run_search(query)

print(f"
Query: {query}
")

for rank, result in enumerate(results, start=1):
    print(f"Result {rank}")
    print(f"Score: {result['_score']:.4f}")
    print("-" * 50)