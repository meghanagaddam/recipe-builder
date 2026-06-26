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

        output_tokens = response.get("eval_count")
        input_tokens = response.get("prompt_eval_count")

        tokens_per_second = None
        eval_duration = response.get("eval_duration")

        if output_tokens and eval_duration:
            tokens_per_second = round(output_tokens / (eval_duration / 1_000_000_000), 2)

        return LLMResponse(
            content=response["message"]["content"],
            metadata=LLMMetadata(
                provider="ollama",
                model=self.model,
                response_time_seconds=round(response_time, 2),
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                total_tokens=(
                    input_tokens + output_tokens
                    if input_tokens is not None and output_tokens is not None
                    else None
                ),
                tokens_per_second=tokens_per_second,
            ),
        )