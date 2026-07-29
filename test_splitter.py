from rag.splitter import split_documents

chunks = split_documents()

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0].page_content)

print("\nSecond Chunk:\n")
print(chunks[1].page_content)