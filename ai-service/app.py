from pipeline.rag_pipeline import RAGPipeline


rag = RAGPipeline()

question = "What projects are mentioned in this document?"

answer = rag.ask(question)

print("\n===== FINAL ANSWER =====\n")
print(answer)