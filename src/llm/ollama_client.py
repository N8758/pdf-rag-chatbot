import ollama

class OllamaClient:

    def __init__(
        self,
        model_name="tinyllama"
    ):

        self.model_name = model_name

    def generate(
        self,
        prompt
    ):

        response = ollama.chat(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]