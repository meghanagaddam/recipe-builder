from recipe_builder.config import DEFAULT_LLM_PROVIDER
from recipe_builder.services.llm.base import BaseLLM
from recipe_builder.services.llm.ollama import OllamaLLM


class LLMFactory:
    @staticmethod
    def create(provider: str = DEFAULT_LLM_PROVIDER) -> BaseLLM:
        provider = provider.lower().strip()

        if provider == "ollama":
            return OllamaLLM()

        raise ValueError(f"Unsupported LLM provider: {provider}")