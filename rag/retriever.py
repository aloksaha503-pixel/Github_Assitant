from langchain_community.vectorstores import FAISS
from rag.embedder import get_embeddings


def get_retriever():
    embeddings = get_embeddings()

    vector_store = FAISS.load_local(
        "vector_db/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 15,
        "lambda_mult": 0.7
    }
    ) 
    

    return retriever