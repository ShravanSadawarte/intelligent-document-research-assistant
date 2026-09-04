from pipeline.rag_pipeline import RAGPipeline


rag = RAGPipeline()

print("\n====================================")
print("   Intelligent Document Assistant")
print("====================================")
print("Ask questions about your document.")
print("Type 'exit' to quit.\n")


while True:
    question = input("You: ").strip()

    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    if not question:
        continue

    try:
        answer = rag.ask(question)

        print("\nAssistant:")
        print(answer)
        print()

    except Exception as e:
        print(f"\nError: {e}\n")