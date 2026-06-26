from recipe_builder.models.llm import LLMResponse
from recipe_builder.models.recipe import RecipeRequest
from recipe_builder.prompts.recipe_prompt import build_recipe_prompt
from recipe_builder.services.llm.base import BaseLLM
from recipe_builder.services.llm.ollama import OllamaLLM


def generate_recipe(
    request: RecipeRequest,
    llm: BaseLLM | None = None,
) -> LLMResponse:
    llm = llm or OllamaLLM()

    prompt = build_recipe_prompt(request)
    return llm.generate(prompt)