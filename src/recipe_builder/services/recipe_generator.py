from recipe_builder.models.llm import LLMResponse
from recipe_builder.models.recipe import RecipeRequest
from recipe_builder.prompts.recipe_prompt import build_recipe_prompt
from recipe_builder.services.llm.base import BaseLLM
from recipe_builder.services.llm.factory import LLMFactory


def generate_recipe(
    request: RecipeRequest,
    llm: BaseLLM | None = None,
    prompt_version: str = "recipe_v1",
) -> LLMResponse:
    llm = llm or LLMFactory.create()

    prompt = build_recipe_prompt(
        request=request,
        prompt_version=prompt_version,
    )

    return llm.generate(prompt)