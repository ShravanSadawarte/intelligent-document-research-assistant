from ingestion.loader import load_pdf
from ingestion.chunker import chunk_pages
from embeddings.embedding_model import EmbeddingModel
from vectorstore.chroma import ChromaVectorStore


# 1. Load PDF
pages = load_pdf("data/sample.pdf")

# 2. Create chunks
chunks = chunk_pages(pages)

print("Pages:", len(pages))
print("Chunks:", len(chunks))


# 3. Generate embeddings
embedding_model = EmbeddingModel()

texts = [chunk["text"] for chunk in chunks]

embeddings = embedding_model.embed_texts(texts)

print("Embeddings:", len(embeddings))
print("Vector dimension:", len(embeddings[0]))


# 4. Store in ChromaDB
vector_store = ChromaVectorStore()

vector_store.add_documents(
    chunks,
    embeddings
)

print("Documents stored:", vector_store.count())