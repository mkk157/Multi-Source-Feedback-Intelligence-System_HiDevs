from src.rag.rag_chain import answer_question


question = "Summarize negative feedback from customers."

response = answer_question(question)

print("\nQuestion:")
print(question)

print("\nResponse:\n")
print(response)