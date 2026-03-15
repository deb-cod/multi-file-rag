import os
import requests
import tempfile

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)

from langchain.schema import Document
from bs4 import BeautifulSoup

from langchain.text_splitter import RecursiveCharacterTextSplitter
from embeddings.embedder import get_embedding_model
from vector_store.qdrant_db_client import store_embeddings


def load_document(path_or_url):
    """Load document from file OR URL"""

    # -------- URL LOADER --------
    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        print("Loading from URL")
        # -------- PDF URL --------
        if path_or_url.lower().endswith(".pdf"):
            response = requests.get(path_or_url)
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
            tmp.write(response.content)
            tmp.close()
            loader = PyPDFLoader(tmp.name)
            return loader.load()
        # -------- Normal HTML page --------
        response = requests.get(
            path_or_url,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator="\n")
        print("Loaded text")
        return [Document(page_content=text, metadata={"path_or_url": path_or_url})]

    # -------- FILE LOADER --------
    ext = os.path.splitext(path_or_url)[1].lower()

    if ext == ".pdf":
        loader = PyPDFLoader(path_or_url)
    elif ext == ".txt":
        loader = TextLoader(path_or_url)
    elif ext == ".docx":
        loader = Docx2txtLoader(path_or_url)
    elif ext in [".html", ".htm"]:
        with open(path_or_url, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
        text = soup.get_text(separator="\n")

        return [Document(page_content=text, metadata={"source": path_or_url})]
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

