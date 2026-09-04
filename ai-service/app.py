from ingestion.loader import load_pdf
from ingestion.chunker import chunk_pages


pdf_path = "data/sample.pdf"

pages = load_pdf(pdf_path)

chunks = chunk_pages(pages)

print(f"Total pages: {len(pages)}")
print(f"Total chunks: {len(chunks)}")

for chunk in chunks[:5]:
    print("\n--------------------")
    print(f"Chunk ID: {chunk['chunk_id']}")
    print(f"Page: {chunk['page_number']}")
    print(chunk["text"])