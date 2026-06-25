from recipe_builder.models.recipe import RecipeRequest


def build_recipe_prompt(request: RecipeRequest) -> str:
    avoid = ", ".join(request.avoid_ingredients) if request.avoid_ingredients else "None"

    return f"""
You are an expert recipe assistant.

Task:
Create a practical recipe using the user's available ingredients.

User Inputs:
- Available ingredients: {", ".join(request.ingredients)}
- Cuisine: {request.cuisine}
- Servings: {request.servings}
- Maximum cooking time: {request.cook_time_minutes} minutes
- Diet preference: {request.diet_preference}
- Spice level: {request.spice_level}
- Ingredients to avoid: {avoid}

Rules:
- Prefer the available ingredients.
- Do not use ingredients listed under "Ingredients to avoid".
- If extra ingredients are needed, mark them as optional.
- Keep the recipe realistic and beginner-friendly.
- Keep nutrition as an estimate only.

Return the response in this format:
1. Recipe Name
2. Short Description
3. Ingredients with quantities
4. Step-by-step Instructions
5. Cooking Time
6. Nutrition Estimate
7. Substitutions
8. Storage Tips
"""