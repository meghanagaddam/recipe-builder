from ollama import chat

from recipe_builder.config import (
    DEFAULT_MODEL,
    OLLAMA_MAX_TOKENS,
    OLLAMA_TEMPERATURE,
)
from recipe_builder.services.llm.base import BaseLLM


class OllamaLLM(BaseLLM):
    def __init__(
        self,
        model: str = DEFAULT_MODEL,
        temperature: float = OLLAMA_TEMPERATURE,
        max_tokens: int = OLLAMA_MAX_TOKENS,
    ):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate(self, prompt: str) -> str:
        response = chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            options={
                "temperature": self.temperature,
                "num_predict": self.max_tokens,
            },
        )

        return response["message"]["content"]