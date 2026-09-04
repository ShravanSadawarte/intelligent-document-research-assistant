from embeddings.embedding_model import EmbeddingModel


model = EmbeddingModel()

texts = [
    "Artificial intelligence is transforming software development.",
    "Retrieval augmented generation uses external knowledge."
]

embeddings = model.embed_texts(texts)

print("Number of embeddings:", len(embeddings))
print("Vector dimension:", len(embeddings[0]))
print("First 5 values:", embeddings[0][:5])