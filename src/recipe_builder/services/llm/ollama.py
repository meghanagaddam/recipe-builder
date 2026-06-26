import time

from ollama import chat

from recipe_builder.config import (
    DEFAULT_MODEL,
    OLLAMA_MAX_TOKENS,
    OLLAMA_TEMPERATURE,
)
from recipe_builder.models.llm import LLMMetadata, LLMResponse
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

    def generate(self, prompt: str) -> LLMResponse:
        start_time = time.perf_counter()

        response = chat(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt},
            ],
            options={
                "temperature": self.temperature,
                "num_predict": self.max_tokens,
            },
        )

        response_time = time.perf_counter() - start_time

        return LLMResponse(
            content=response["message"]["content"],
            metadata=LLMMetadata(
                model=self.model,
                response_time_seconds=round(response_time, 2),
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            ),
        )