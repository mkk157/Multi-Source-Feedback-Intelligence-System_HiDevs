from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def get_embeddings():

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def create_vector_store(chunks):

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory="chroma_db"
    )

    return vector_store


def load_vector_store():

    return Chroma(
        persist_directory="chroma_db",
        embedding_function=get_embeddings()
    )