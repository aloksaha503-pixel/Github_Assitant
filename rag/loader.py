from langchain_community.document_loaders import TextLoader


def load_documents():
    loader = TextLoader("data/git_knowledge.md", encoding="utf-8")
    documents = loader.load()
    return documents