import streamlit as st
import requests


# -----------------------------------
# FastAPI backend URL
# -----------------------------------
BASE_URL = "http://127.0.0.1:8000"


# -----------------------------------
# Page config
# -----------------------------------
st.set_page_config(
    page_title="Hybrid Semantic Search Engine",
    page_icon="🔎",
    layout="wide"
)


# -----------------------------------
# Title
# -----------------------------------
st.title("🔎 Hybrid Semantic Search Engine")

st.markdown("""
Production-inspired retrieval system combining:

- BM25 lexical retrieval
- Semantic vector search
- Hybrid ranking fusion
""")


# -----------------------------------
# Sidebar
# -----------------------------------
st.sidebar.header("Search Settings")

search_mode = st.sidebar.selectbox(
    "Retrieval Mode",
    ["BM25", "Semantic", "Hybrid"]
)

top_k = st.sidebar.slider(
    "Top K Results",
    min_value=1,
    max_value=20,
    value=10
)


# -----------------------------------
# Query Input
# -----------------------------------
query = st.text_input(
    "Enter your search query",
    placeholder="e.g. artificial intelligence"
)


# -----------------------------------
# Search button
# -----------------------------------
search_clicked = st.button("Search")


# -----------------------------------
# Endpoint mapping
# -----------------------------------
endpoint_map = {
    "BM25": "/search",
    "Semantic": "/semantic-search",
    "Hybrid": "/hybrid-search"
}


# -----------------------------------
# Search logic
# -----------------------------------
if search_clicked and query.strip():

    endpoint = endpoint_map[search_mode]

    url = f"{BASE_URL}{endpoint}"

    params = {
        "query": query,
        "k": top_k
    }

    with st.spinner("Retrieving results..."):

        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:

                results = response.json()

                st.success(f"Retrieved {len(results)} results")

                # -----------------------------------
                # Display Results
                # -----------------------------------
                for idx, result in enumerate(results, start=1):

                    doc_id = result.get("doc_id", "N/A")

                    score = (
                        result.get("score")
                        or result.get("hybrid_score")
                        or "N/A"
                    )

                    text = result.get("text", "")

                    with st.container():

                        st.markdown(f"## Result {idx}")

                        col1, col2 = st.columns([1, 1])

                        with col1:
                            st.markdown(f"**Document ID:** {doc_id}")

                        with col2:
                            st.markdown(f"**Score:** {score}")

                        st.markdown("### Preview")

                        preview = text[:500]

                        st.write(preview)

                        st.divider()

            else:
                st.error(
                    f"API Error: {response.status_code}"
                )

                st.text(response.text)

        except Exception as e:

            st.error("Failed to connect to FastAPI backend")

            st.exception(e)


# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")

st.markdown("""
Built with:

- FastAPI
- ElasticSearch
- FAISS
- Sentence Transformers
- Streamlit
""")