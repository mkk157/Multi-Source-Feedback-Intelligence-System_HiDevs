from src.embeddings.vector_store import load_vector_store


def retrieve_feedback(query, k=5):

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_kwargs={
            "k": k
        }
    )

    results = retriever.invoke(query)

    return results


def retrieve_feedback_by_category(query, category, k=5):

    vector_store = load_vector_store()

    results = vector_store.similarity_search(
        query=query,
        k=k,
        filter={
            "rating_category": category
        }
    )

    return results