from qdrant_client import QdrantClient
from embeddings.embedder import get_embedding_model

client = QdrantClient("localhost", port=6333)

COLLECTION_NAME = "documents"


def retrieve(query, k=5):

    embedder = get_embedding_model()

    query_vector = embedder.encode(query)

    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=k
    )

    docs = [r.payload["text"] for r in results]

    return docs