def build_rag_prompt(question: str, retrieved_results: dict) -> str:
    """
    Build a prompt for the LLM using retrieved document chunks.
    """

    documents = retrieved_results["documents"][0]
    metadatas = retrieved_results["metadatas"][0]

    context_parts = []

    for i, (document, metadata) in enumerate(
        zip(documents, metadatas),
        start=1
    ):
        page_number = metadata.get("page_number", "Unknown")

        context_parts.append(
            f"[Context {i} | Page {page_number}]\n"
            f"{document}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are a document research assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the answer cannot be found in the context, say:
"I could not find the answer in the provided document."

Do not make up information.

Context:
--------------------
{context}
--------------------

User Question:
{question}

Answer:
"""

    return prompt