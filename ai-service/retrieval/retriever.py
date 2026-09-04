from embeddings.embedding_model import EmbeddingModel
from vectorstore.chroma import ChromaVectorStore


class Retriever:
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = ChromaVectorStore()

    def retrieve(self, query: str, top_k: int = 5):
        # Convert the user's question into a vector
        query_embedding = self.embedding_model.embed_query(query)

        # Search ChromaDB
        results = self.vector_store.search(
            query_embedding,
            top_k
        )

        return results