import pandas as pd

from src.chunking.text_chunker import (
    create_documents,
    create_chunks
)

from src.embeddings.vector_store import (
    create_vector_store
)

df = pd.read_csv(
    "data/processed/cleaned_feedback.csv"
)

documents = create_documents(df)

chunks = create_chunks(documents)

print("Documents:", len(documents))
print("Chunks:", len(chunks))

vector_store = create_vector_store(chunks)

print("\nVector Store Created Successfully")