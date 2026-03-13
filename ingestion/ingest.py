from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from embeddings.embedder import get_embedding_model
from vector_store.qdrant_db_client import store_embeddings

def ingest_document(path):
    loader = UnstructuredFileLoader(path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)
    embedder = get_embedding_model()
    texts = [c.page_content for c in chunks]
    vectors = embedder.encode(texts)
    store_embeddings(path, vectors)

