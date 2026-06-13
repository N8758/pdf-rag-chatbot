import chromadb


class ChromaClient:

    def __init__(
        self,
        db_path="chroma_db",
        collection_name="pdf_knowledge_base"
    ):

        self.client = chromadb.PersistentClient(
            path=db_path
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def get_collection(self):
        return self.collection