from src.embeddings.embedding_model import EmbeddingModel
from src.vectordb.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        self.vector_store = VectorStore()

    def retrieve(
        self,
        query,
        top_k=5
    ):

        query_embedding = self.embedding_model.embed_query(
            query
        )

        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        formatted_results = []

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        for doc, metadata, distance in zip(
            documents,
            metadatas,
            distances
        ):

            formatted_results.append(
                {
                    "content": doc,
                    "metadata": metadata,
                    "score": round(
                        1 - distance,
                        4
                    )
                }
            )

        return formatted_results