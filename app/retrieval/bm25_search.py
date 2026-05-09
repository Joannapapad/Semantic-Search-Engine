from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

INDEX_NAME = "documents"

def bm25_search(query, k=20):

    response = es.search(
        index=INDEX_NAME,
        size=k,
        query={
            "match": {
                "text": query
            }
        }
    )

    results = []

    for hit in response["hits"]["hits"]:

        results.append({
            "doc_id": hit["_id"],
            "score": hit["_score"],
            "text": hit["_source"]["text"][:300]
        })

    return results