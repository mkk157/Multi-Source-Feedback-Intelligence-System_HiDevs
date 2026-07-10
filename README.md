# Multi-Source Feedback Intelligence System

This project is automatically generated.

## Installation

```sh
pip install -r requirements.txt
```

## Step 3 - Splitting and Chunking

The RecursiveCharacterTextSplitter was selected based on the
HiDevs recommendation that it is a general-purpose splitter
capable of maintaining semantic coherence across document types.

Chunk size was configured at 500 characters with 100-character
overlap.

Since customer reviews are typically short, most reviews resulted
in a one-to-one mapping between documents and chunks.

## Step 5 - Query Processing and AI Engine

In this step, the system processes user questions and retrieves relevant
customer feedback from the ChromaDB vector database using semantic search.

The retrieved feedback is passed as context to the Groq-hosted Llama 3 model
through a LangChain prompt template. The model generates a context-aware
response based only on the retrieved customer feedback.

This step completes the core Retrieval-Augmented Generation pipeline:

User Query → Retriever → ChromaDB → Prompt Template → Groq Llama 3 → Response