from qdrant_client import QdrantClient

client = QdrantClient("localhost", port=6333)

def store_embeddings(texts, vectors):

    points = []

    for i in range(len(texts)):
        points.append({
            "id": i,
            "vector": vectors[i],
            "payload": {"text": texts[i]}
        })

    client.upsert(
        collection_name="documents",
        points=points
    )

