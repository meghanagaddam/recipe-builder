from recipe_builder.models.recipe import RecipeRequest
from recipe_builder.prompts.registry import PromptRegistry


def build_recipe_prompt(request: RecipeRequest, prompt_version: str = "recipe_v2") -> str:
    template = PromptRegistry.load(prompt_version)

    ingredients = ", ".join(request.ingredients) if request.ingredients else "Not explicitly provided"
    avoid_ingredients = (
        ", ".join(request.avoid_ingredients)
        if request.avoid_ingredients
        else "None"
    )

    return template.replace("{{user_request}}", request.user_request or "Not provided") \
        .replace("{{ingredients}}", ingredients) \
        .replace("{{cuisine}}", request.cuisine) \
        .replace("{{servings}}", str(request.servings)) \
        .replace("{{cook_time_minutes}}", str(request.cook_time_minutes)) \
        .replace("{{diet_preference}}", request.diet_preference) \
        .replace("{{spice_level}}", request.spice_level) \
        .replace("{{avoid_ingredients}}", avoid_ingredients)