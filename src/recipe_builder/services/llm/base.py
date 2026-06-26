from abc import ABC, abstractmethod

from recipe_builder.models.llm import LLMResponse


class BaseLLM(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> LLMResponse:
        """Generate text from a prompt."""
        pass