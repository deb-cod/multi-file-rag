from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

client = QdrantClient("localhost", port=6333)

COLLECTION_NAME = "documents"
VECTOR_SIZE = 384   # bge-small-en embedding size


def create_collection_if_not_exists():
    collections = client.get_collections().collections
    collection_names = [c.name for c in collections]

    if COLLECTION_NAME not in collection_names:
        print("Creating Qdrant collection...")

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=VECTOR_SIZE,
                distance=Distance.COSINE
            )
        )


def store_embeddings(path, texts, vectors):

    create_collection_if_not_exists()

    points = []

    import uuid
    import os

    file_name = os.path.basename(path)

    for i in range(len(texts)):
        points.append({
            "id": str(uuid.uuid4()),
            "vector": vectors[i],
            "payload": {
                "text": texts[i],
                "source": file_name,
                "chunk": i
            }
        })

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print(f"Stored {len(points)} vectors in Qdrant")