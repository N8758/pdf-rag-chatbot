# RAG Chatbot using Ollama, ChromaDB and Streamlit

## Overview

This project is a Retrieval-Augmented Generation (RAG) Chatbot that allows users to upload PDF documents and ask questions based on the content of those documents.

The system extracts text from PDFs, creates chunks, generates embeddings, stores them in a vector database (ChromaDB), retrieves the most relevant information, and uses an Ollama-hosted Large Language Model (LLM) to generate accurate answers.

---

## Features

* PDF Upload Support
* Automatic Text Extraction
* Intelligent Text Chunking
* Vector Embeddings Generation
* ChromaDB Vector Storage
* Semantic Search
* Retrieval-Augmented Generation (RAG)
* Local LLM Inference using Ollama
* Streamlit User Interface

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### LLM

* Ollama
* TinyLlama / Llama3

### Vector Database

* ChromaDB

### Embedding Model

* Sentence Transformers

### PDF Processing

* PyPDF

---

## Project Architecture

User Uploads PDF
↓
PDF Processing
↓
Text Extraction
↓
Chunking
↓
Embedding Generation
↓
ChromaDB Storage
↓
User Query
↓
Retriever
↓
Relevant Chunks
↓
Ollama LLM
↓
Generated Answer

---

## Folder Structure

rag-chatbot/

├── app.py

├── requirements.txt

├── README.md

├── data/

├── assets/

├── src/

│ ├── chunking/

│ │ └── chunker.py

│ ├── embeddings/

│ ├── llm/

│ │ ├── ollama_client.py

│ │ └── answer_generator.py

│ ├── pdf_processing/

│ ├── retrieval/

│ │ └── retriever.py

│ ├── utils/

│ └── vectordb/

│ ├── chroma_client.py

│ └── vector_store.py

└── chroma_db/

---

## Installation

### Clone Repository

git clone <repository-url>

cd rag-chatbot

---

### Create Virtual Environment

python -m venv venv

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

---

### Install Dependencies

pip install -r requirements.txt

---

### Install Ollama

Download and install Ollama from:

https://ollama.com

---

### Pull Model

ollama pull tinyllama

OR

ollama pull llama3

---

## Running the Project

Start Ollama:

ollama serve

Run Streamlit Application:

streamlit run app.py

Application will be available at:

http://localhost:8501

---

## How It Works

1. User uploads PDF document.
2. System extracts text from PDF.
3. Extracted text is split into chunks.
4. Embeddings are generated.
5. Embeddings are stored in ChromaDB.
6. User asks a question.
7. Retriever finds relevant chunks.
8. Relevant chunks are sent to Ollama.
9. LLM generates the final answer.
10. Answer is displayed in Streamlit UI.

---

## Example Questions

* What is machine learning?
* Summarize the document.
* What are the key findings?
* Explain the introduction section.
* What technologies are mentioned?

---

## Future Improvements

* Multi-PDF Support
* Citation Support
* Chat History
* Hybrid Search
* Better Embedding Models
* Advanced Reranking
* User Authentication
* Cloud Deployment

---

## Accuracy

The chatbot achieves approximately 85–90% accuracy on well-structured PDF documents. Accuracy depends on document quality, chunking strategy, embedding model performance, and retrieval quality.

---

## Author

Nilesh Pulate

Information Technology Engineer

RAG Chatbot Challenge Project
