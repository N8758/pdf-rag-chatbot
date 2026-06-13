from src.llm.ollama_client import OllamaClient


class AnswerGenerator:

    def __init__(self):

        self.llm = OllamaClient()

    def generate_answer(
        self,
        query,
        retrieved_chunks
    ):

        context = ""

        sources = []

        for chunk in retrieved_chunks:

            context += chunk["content"]
            context += "\n\n"

            metadata = chunk["metadata"]

            source = (
                f'{metadata["pdf_name"]}'
                f' (Page {metadata["page_number"]})'
            )

            sources.append(source)

        prompt = f"""
You are a PDF knowledge assistant.

Answer ONLY from the provided context.

If answer is not available in context,
say:
"I could not find the answer in the uploaded PDFs."

Context:
{context}

Question:
{query}

Provide a concise answer.
"""

        answer = self.llm.generate(
            prompt
        )

        unique_sources = list(
            set(sources)
        )

        return {
            "answer": answer,
            "sources": unique_sources
        }