import pandas as pd

from src.chunking.text_chunker import (
    create_documents,
    create_chunks
)

df = pd.read_csv(
    "data/processed/cleaned_feedback.csv"
)

documents = create_documents(df)

chunks = create_chunks(documents)

print("\nTotal Reviews:")
print(len(df))

print("\nDocuments Created:")
print(len(documents))

print("\nChunks Created:")
print(len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0].page_content)

print("\nMetadata:\n")
print(chunks[0].metadata)