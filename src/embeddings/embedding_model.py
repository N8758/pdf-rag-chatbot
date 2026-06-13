from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(
        self,
        model_name="BAAI/bge-small-en-v1.5"
    ):
        self.model = SentenceTransformer(model_name)

    def generate_embedding(
        self,
        text
    ):
        """
        Generate embedding for a single text.
        """

        embedding = self.model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding.tolist()

    def generate_embeddings(
        self,
        texts
    ):
        """
        Generate embeddings for multiple texts.
        """

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True
        )

        return embeddings.tolist()

    def embed_chunks(
        self,
        chunks
    ):
        """
        Input:
            chunks = [
                {
                    "chunk_id": "...",
                    "content": "...",
                    "metadata": {...}
                }
            ]

        Output:
            chunks with embeddings
        """

        contents = [
            chunk["content"]
            for chunk in chunks
        ]

        embeddings = self.generate_embeddings(
            contents
        )

        embedded_chunks = []

        for chunk, embedding in zip(
            chunks,
            embeddings
        ):
            embedded_chunks.append(
                {
                    "chunk_id": chunk["chunk_id"],
                    "content": chunk["content"],
                    "metadata": chunk["metadata"],
                    "embedding": embedding
                }
            )

        return embedded_chunks

    def embed_query(
        self,
        query
    ):
        """
        Generate embedding for user query.
        """

        return self.generate_embedding(query)