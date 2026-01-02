from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct


class QdrantStorage:
    def __init__(self, url="http://localhost:6333", collection="docs", dim=3072):
        self.client = QdrantClient(host="localhost", port=6333, timeout=30)
        self.collection = collection
        if not self.client.collection_exists(self.collection):
            self.client.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
            )

    def upsert(self, ids, vectors, payloads):
        print(vectors)
        print("##############")
        print(payloads)
        points = [PointStruct(id=ids[i], vector=vectors[i], payload=payloads[i]) for i in range(len(ids))]
        self.client.upsert(self.collection, points=points)

    def delete_all(self):
        self.client.delete_collection(self.collection)
        self.client.create_collection(
            collection_name=self.collection,
            vectors_config=VectorParams(size=3072, distance=Distance.COSINE),
        )

    def search(self, query_vector, top_k: int = 5):
        print(type(self.client))
        print(self.client.__class__.__module__)
        print("search" in dir(self.client))

        results = self.client.query_points(
            collection_name=self.collection,
            query=query_vector,
            with_payload=True,
            limit=top_k
        )
        
        contexts = []
        sources = set()

        # for r in results:
        #     payload = getattr(r, "payload", None) or {}
        #     text = payload.get("text", "")
        #     source = payload.get("source", "")
        #     if text:
        #         contexts.append(text)
        #         sources.add(source)
        
        for point in getattr(results, "points", []):
            payload = point.payload or {}
            text = payload.get("text", "")
            if text:
                contexts.append(text)


        return {"contexts": contexts, "sources": list(sources)}