import os

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)

from langchain.text_splitter import RecursiveCharacterTextSplitter
from embeddings.embedder import get_embedding_model
from vector_store.qdrant_db_client import store_embeddings


def load_document(path):
    """Select appropriate loader based on file type"""

    ext = os.path.splitext(path)[1].lower()

    if ext == ".pdf":
        loader = PyPDFLoader(path)

    elif ext == ".txt":
        loader = TextLoader(path)

    elif ext == ".docx":
        loader = Docx2txtLoader(path)

    else:
        raise ValueError(f"Unsupported file type: {ext}")

    return loader.load()


def ingest_document(path):

    print(f"Loading document: {path}")

    docs = load_document(path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    embedder = get_embedding_model()

    texts = [c.page_content for c in chunks]

    vectors = embedder.encode(texts)

    # store both texts and vectors
    store_embeddings(path, texts, vectors)

    print(f"Ingested {len(texts)} chunks from {path}")

