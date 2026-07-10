from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from src.rag.retriever import retrieve_feedback, retrieve_feedback_by_category
from src.rag.prompt_template import feedback_prompt

load_dotenv()


def format_documents(docs):

    formatted_docs = []

    for doc in docs:

        source = doc.metadata.get("source", "Unknown")
        rating = doc.metadata.get("rating", "Unknown")
        rating_category = doc.metadata.get(
            "rating_category",
            "Unknown"
        )

        formatted_text = f"""
Source: {source}
Rating: {rating}
Rating Category: {rating_category}
Feedback: {doc.page_content}
"""

        formatted_docs.append(formatted_text)

    return "\n\n".join(formatted_docs)


def answer_question(question):

    question_lower = question.lower()

    if "negative" in question_lower:
        docs = retrieve_feedback_by_category(
            query=question,
            category="Negative"
        )

    elif "positive" in question_lower:
        docs = retrieve_feedback_by_category(
            query=question,
            category="Positive"
        )

    elif "neutral" in question_lower:
        docs = retrieve_feedback_by_category(
            query=question,
            category="Neutral"
        )

    else:
        docs = retrieve_feedback(question)

    context = format_documents(docs)

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )

    chain = (
        feedback_prompt
        | llm
        | StrOutputParser()
    )

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response