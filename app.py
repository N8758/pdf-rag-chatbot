import streamlit as st
import os

from src.pdf_processing.pdf_extractor import PDFExtractor
from src.pdf_processing.text_cleaner import TextCleaner

from src.chunking.chunker import TextChunker

from src.embeddings.embedding_model import EmbeddingModel

from src.vectordb.vector_store import VectorStore

from src.retrieval.retriever import Retriever

from src.llm.answer_generator import AnswerGenerator


st.set_page_config(
    page_title="RAG Chatbot",
    layout="wide"
)

st.title("📚 PDF RAG Chatbot")

os.makedirs("data/pdfs", exist_ok=True)


# ----------------------------------
# SIDEBAR
# ----------------------------------

st.sidebar.header("Upload PDFs")

uploaded_files = st.sidebar.file_uploader(
    "Choose PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)


# ----------------------------------
# INGESTION
# ----------------------------------

if st.sidebar.button("Process PDFs"):

    if not uploaded_files:
        st.warning("Please upload PDFs first.")
        st.stop()

    embedding_model = EmbeddingModel()
    vector_store = VectorStore()

    total_chunks = 0

    progress_bar = st.progress(0)

    for index, pdf_file in enumerate(uploaded_files):

        pdf_path = os.path.join(
            "data/pdfs",
            pdf_file.name
        )

        with open(pdf_path, "wb") as f:
            f.write(pdf_file.getbuffer())

        pages = PDFExtractor.extract_text(
            pdf_path
        )

        for page in pages:

            page["text"] = TextCleaner.clean(
                page["text"]
            )

        chunker = TextChunker(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = chunker.create_chunks(
            pages=pages,
            pdf_name=pdf_file.name
        )

        embedded_chunks = embedding_model.embed_chunks(
            chunks
        )

        vector_store.add_chunks(
            embedded_chunks
        )

        total_chunks += len(chunks)

        progress_bar.progress(
            (index + 1) / len(uploaded_files)
        )

    st.success(
        f"Ingestion Complete! {total_chunks} chunks indexed."
    )


# ----------------------------------
# CHAT
# ----------------------------------

st.divider()

st.subheader("Ask Questions")

question = st.text_input(
    "Enter your question"
)

if st.button("Ask"):

    if not question:
        st.warning("Enter a question.")
        st.stop()

    retriever = Retriever()

    retrieved_chunks = retriever.retrieve(
        query=question,
        top_k=5
    )

    generator = AnswerGenerator()

    result = generator.generate_answer(
        query=question,
        retrieved_chunks=retrieved_chunks
    )

    st.subheader("Answer")

    st.write(
        result["answer"]
    )

    st.subheader("Sources")

    for source in result["sources"]:
        st.write(
            f"📄 {source}"
        )

    st.subheader("Retrieved Chunks")

    for index, chunk in enumerate(
        retrieved_chunks,
        start=1
    ):

        with st.expander(
            f"Chunk {index}"
        ):

            st.write(
                f"Score: {chunk['score']}"
            )

            st.write(
                chunk["content"]
            )

            st.write(
                chunk["metadata"]
            )


# ----------------------------------
# FOOTER
# ----------------------------------

st.divider()

st.caption(
    "RAG Chatbot | Streamlit + ChromaDB + Ollama"
)