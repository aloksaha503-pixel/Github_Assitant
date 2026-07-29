from langchain_community.vectorstores import FAISS
from rag.splitter import split_documents
from rag.embedder import get_embeddings


def create_vector_store():
    chunks = split_documents()
    embeddings = get_embeddings()

    vector_store = FAISS.from_documents(chunks, embeddings)

    vector_store.save_local("vector_db/faiss_index")

    print("✅ Vector database created successfully!")


if __name__ == "__main__":
    create_vector_store()