from langchain_core.documents import Document
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


def create_documents(df):

    documents = []

    for _, row in df.iterrows():

        doc = Document(
            page_content=str(row["feedback_text"]),
            metadata={
                "source": row["source"],
                "rating": row["rating"],
                "rating_category": row["rating_category"]
            }
        )

        documents.append(doc)

    return documents


def create_chunks(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(
        documents
    )

    return chunks