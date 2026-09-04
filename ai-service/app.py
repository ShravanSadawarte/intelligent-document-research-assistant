from retrieval.retriever import Retriever


retriever = Retriever()

query = "What is the main purpose of this document?"

results = retriever.retrieve(
    query=query,
    top_k=3
)

print("\nQuery:")
print(query)

print("\nRetrieved chunks:\n")

for i, document in enumerate(results["documents"][0], start=1):
    metadata = results["metadatas"][0][i - 1]

    print(f"--- Result {i} ---")
    print(f"Page: {metadata['page_number']}")
    print(document)
    print()