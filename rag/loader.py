from langchain_community.document_loaders import DirectoryLoader,TextLoader


def load_documents():
    loader = DirectoryLoader(
        "data",
        glob="*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}
    )

    documents = loader.load()
    return documents