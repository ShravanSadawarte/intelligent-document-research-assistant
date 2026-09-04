def chunk_pages(
    pages: list[dict],
    chunk_size: int = 500,
    chunk_overlap: int = 50
) -> list[dict]:
    """
    Split page text into overlapping chunks.

    Each chunk keeps its original page number.
    """

    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size.")

    chunks = []

    for page in pages:
        text = page["text"]
        page_number = page["page_number"]

        if not text:
            continue

        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end].strip()

            if chunk_text:
                chunks.append({
                    "chunk_id": len(chunks),
                    "page_number": page_number,
                    "text": chunk_text
                })

            start += chunk_size - chunk_overlap

    return chunks