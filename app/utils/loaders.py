import pandas as pd
from app.utils.preprocessing import clean_text

def load_documents(path):
    df = pd.read_csv(path)

    df["Text"] = df["Text"].astype(str).apply(clean_text)

    document_ids = df["ID"].tolist()
    document_texts = df["Text"].tolist()

    return document_ids, document_texts

def load_queries(path):
    df = pd.read_csv(path)

    df["Text"] = df["Text"].astype(str).apply(clean_text)

    query_ids = df["ID"].tolist()
    query_texts = df["Text"].tolist()

    return query_ids, query_texts