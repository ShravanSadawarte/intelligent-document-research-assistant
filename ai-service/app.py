from generation.llm import LLM


llm = LLM()

prompt = """
Explain what Retrieval-Augmented Generation (RAG) is
in 3 simple sentences.
"""

answer = llm.generate(prompt)

print("\nLLM RESPONSE:")
print(answer)