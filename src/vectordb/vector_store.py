from src.vectordb.chroma_client import ChromaClient


class VectorStore:

    def __init__(self):

        chroma = ChromaClient()

        self.collection = chroma.get_collection()

    def add_chunks(
        self,
        embedded_chunks
    ):

        ids = []
        documents = []
        metadatas = []
        embeddings = []

        for chunk in embedded_chunks:

            ids.append(
                chunk["chunk_id"]
            )

            documents.append(
                chunk["content"]
            )

            metadatas.append(
                chunk["metadata"]
            )

            embeddings.append(
                chunk["embedding"]
            )

        self.collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=embeddings
        )

    def search(
        self,
        query_embedding,
        top_k=5
    ):

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results

    def count_documents(self):

        return self.collection.count()