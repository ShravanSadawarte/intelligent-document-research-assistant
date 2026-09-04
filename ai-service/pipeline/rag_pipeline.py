from retrieval.retriever import Retriever
from generation.prompt import build_rag_prompt
from generation.llm import LLM


class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLM()

    def ask(self, question: str, top_k: int = 5) -> str:
        """
        Execute the complete RAG pipeline.

        Flow:
        Question
            ↓
        Retrieval
            ↓
        Context construction
            ↓
        Prompt
            ↓
        LLM
            ↓
        Answer
        """

        # 1. Retrieve relevant document chunks
        retrieved_results = self.retriever.retrieve(
            query=question,
            top_k=top_k
        )

        # 2. Build RAG prompt using retrieved context
        prompt = build_rag_prompt(
            question,
            retrieved_results
        )

        # 3. Generate answer using the LLM
        answer = self.llm.generate(prompt)

        return answer