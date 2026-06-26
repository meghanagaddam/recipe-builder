from recipe_builder.config import DEFAULT_LLM_PROVIDER, DEFAULT_MODEL, OLLAMA_TEMPERATURE, OLLAMA_MAX_TOKENS
from recipe_builder.services.llm.base import BaseLLM
from recipe_builder.services.llm.ollama import OllamaLLM


class LLMFactory:
    @staticmethod
    def create(
        provider: str = DEFAULT_LLM_PROVIDER,
        model: str = DEFAULT_MODEL,
        temperature: float = OLLAMA_TEMPERATURE,
        max_tokens: int = OLLAMA_MAX_TOKENS,
    ) -> BaseLLM:
        provider = provider.lower().strip()

        if provider == "ollama":
            return OllamaLLM(
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
            )

        raise ValueError(f"Unsupported LLM provider: {provider}")