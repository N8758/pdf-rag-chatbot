from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextChunker:

    def __init__(
        self,
        chunk_size=1000,
        chunk_overlap=200
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len
        )

    def create_chunks(
        self,
        pages,
        pdf_name
    ):
        """
        pages format:

        [
            {
                "page_number": 1,
                "text": "some text..."
            },
            {
                "page_number": 2,
                "text": "some text..."
            }
        ]
        """

        chunks = []

        for page in pages:

            page_number = page["page_number"]
            text = page["text"]

            if not text or not text.strip():
                continue

            split_chunks = self.splitter.split_text(text)

            for chunk_index, chunk_text in enumerate(split_chunks):

                chunks.append(
                    {
                        "chunk_id": f"{pdf_name}_{page_number}_{chunk_index}",

                        "content": chunk_text,

                        "metadata": {
                            "pdf_name": pdf_name,
                            "page_number": page_number,
                            "chunk_index": chunk_index
                        }
                    }
                )

        return chunks