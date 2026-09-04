from retrieval.retriever import Retriever


retriever = Retriever()

query = "What is the main purpose of this document?"

results = retriever.retrieve(
    query=query,
    top_k=5
)

print("\nQuery:")
print(query)

print("\nRetrieved chunks:\n")

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

for i, document in enumerate(documents, start=1):
    print(f"--- Result {i} ---")
    print(f"Distance: {distances[i - 1]:.4f}")
    print(f"Page: {metadatas[i - 1]['page_number']}")
    print(document)
    print()