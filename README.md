# Hybrid Semantic Search Engine

A production-inspired information retrieval system combining:

* BM25 lexical retrieval
* Dense semantic retrieval
* FAISS vector indexing
* Hybrid ranking pipelines
* FastAPI backend infrastructure

Built using:

* FastAPI
* Sentence Transformers
* FAISS
* ElasticSearch
* Docker
* Streamlit

---

# Overview

This project implements a modular search engine architecture inspired by modern retrieval systems used in large-scale search and recommendation platforms.

The system supports:

* Lexical search using BM25 and ElasticSearch
* Semantic vector retrieval using Sentence Transformers and FAISS
* Hybrid retrieval pipelines combining lexical and semantic ranking
* Evaluation using MAP and ranking metrics
* API-based retrieval endpoints using FastAPI

The project evolved from an academic information retrieval system into a backend-oriented semantic search platform with production-style architecture.

---

# System Architecture

```text
                        ┌─────────────────┐
                        │   User Query    │
                        └────────┬────────┘
                                 │
                                 ▼
                    ┌─────────────────────┐
                    │     FastAPI API     │
                    └────────┬────────────┘
                             │
        ┌────────────────────┴────────────────────┐
        ▼                                         ▼

┌───────────────────┐               ┌────────────────────┐
│ BM25 Retrieval    │               │ Semantic Retrieval │
│ ElasticSearch     │               │ FAISS + Embeddings │
└───────────────────┘               └────────────────────┘
        │                                         │
        └────────────────────┬────────────────────┘
                             ▼

                  ┌─────────────────────┐
                  │ Hybrid Ranking      │
                  │ + Result Scoring    │
                  └─────────────────────┘
```

---

# Features

## Semantic Retrieval

* SentenceTransformer embeddings
* Dense vector search using FAISS
* Cosine similarity retrieval
* Fast nearest-neighbor search

## BM25 Retrieval

* ElasticSearch indexing
* Lexical matching
* Traditional probabilistic retrieval

## Hybrid Search

* Combines lexical and semantic ranking
* Reciprocal Rank Fusion (RRF)
* Production-inspired retrieval pipeline

## FastAPI Backend

* REST API endpoints
* Swagger/OpenAPI documentation
* Modular routing structure

## Evaluation

* MAP evaluation
* Precision metrics
* Retrieval comparison analysis

---

# Project Structure

```text
semantic-search-engine/
│
├── app/
│   ├── api/
│   │   └── routes.py
│   │
│   ├── indexing/
│   │   ├── elasticsearch_indexer.py
│   │   └── faiss_indexer.py
│   │
│   ├── retrieval/
│   │   ├── bm25_search.py
│   │   ├── semantic_search.py
│   │   └── hybrid_search.py
│   │
│   ├── embeddings/
│   │   ├── embedding_model.py
│   │   └── generate_embeddings.py
│   │
│   ├── evaluation/
│   │   ├── generate_run_files.py
│   │   ├── evaluate.py
│   │   └── metrics_visualization.py
│   │
│   ├── utils/
│   │   ├── config.py
│   │   ├── loaders.py
│   │   └── preprocessing.py
│   │
│   └── main.py
│
├── data/
├── frontend/
├── tests/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# Retrieval Pipeline

## Semantic Search Pipeline

```text
Documents
→ SentenceTransformer Embeddings
→ FAISS Vector Index
→ Similarity Search
→ Ranked Results
```

### Embedding Model

The project uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

for efficient dense vector generation.

### Vector Search

FAISS is used for:

* vector indexing
* similarity search
* fast nearest-neighbor retrieval

using inner-product similarity on normalized embeddings.

---

# Hybrid Retrieval

The hybrid search pipeline combines:

* BM25 lexical matching
* semantic vector retrieval

using Reciprocal Rank Fusion (RRF).

This approach improves retrieval robustness by combining:

## BM25 strengths

* lexical overlap
* exact keyword matching
* strong performance on domain-specific datasets

## Semantic retrieval strengths

* contextual similarity
* paraphrase understanding
* semantic matching

---

# API Endpoints

After starting the FastAPI server:

```bash
python -m uvicorn app.main:app --reload
```

Swagger documentation becomes available at:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

### Health Check

```http
GET /health
```

### BM25 Search

```http
GET /search
```

### Semantic Search

```http
GET /semantic-search
```

### Hybrid Search

```http
GET /hybrid-search
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository-url>
cd semantic-search-engine
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```powershell
.\venv\Scripts\Activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Generating Embeddings

```bash
python -m app.embeddings.generate_embeddings
```

This creates:

```text
data/embeddings.npy
```

---

# Building FAISS Index

```bash
python -m app.indexing.faiss_indexer
```

This creates:

```text
data/faiss.index
```

---

# Running the API

```bash
python -m uvicorn app.main:app --reload
```

---

# Evaluation

The project includes retrieval evaluation using:

* MAP
* Precision@K
* ranking comparisons

Example semantic retrieval performance:

| K  | MAP    |
| -- | ------ |
| 20 | 0.3129 |
| 30 | 0.3413 |
| 50 | 0.3744 |

---

# Engineering Design Decisions

## Why Hybrid Retrieval?

Pure semantic retrieval does not always outperform BM25 on structured or domain-specific datasets.

BM25 often performs strongly when:

* queries share exact lexical overlap with documents
* domain terminology is important
* keyword precision matters

Semantic retrieval improves:

* contextual matching
* paraphrase understanding
* semantic similarity

Combining both approaches provides a more robust retrieval system.

---

# Future Improvements

* Cross-encoder reranking
* Query expansion
* Distributed vector databases
* GPU acceleration
* Authentication and rate limiting
* Full frontend deployment
* Retrieval analytics dashboard

---

# Technologies Used

| Category        | Technologies          |
| --------------- | --------------------- |
| Backend         | FastAPI               |
| Semantic Search | Sentence Transformers |
| Vector Search   | FAISS                 |
| Lexical Search  | ElasticSearch         |
| Frontend        | Streamlit             |
| Evaluation      | trec_eval             |
| Deployment      | Docker                |

---

# Current Status

## Completed

* Modular backend architecture
* Semantic retrieval pipeline
* FAISS indexing
* FastAPI backend
* Swagger/OpenAPI docs
* Hybrid retrieval structure
* Evaluation framework

## In Progress

* ElasticSearch integration
* Streamlit frontend
* Docker deployment
* Hybrid reranking improvements

---

# Screenshots

* Swagger API docs
* Semantic search results
* Hybrid search results
* Evaluation graphs
* Frontend UI

---
