from recipe_builder.models.recipe import RecipeRequest


def build_recipe_prompt(request: RecipeRequest) -> str:
    ingredients = ", ".join(request.ingredients) if request.ingredients else "Not explicitly provided"
    avoid = ", ".join(request.avoid_ingredients) if request.avoid_ingredients else "None"

    return f"""
You are an expert recipe assistant.

Task:
Create a practical recipe based on the user's natural language request and optional filters.

User Natural Language Request:
{request.user_request or "Not provided"}

Optional Structured Inputs:
- Available ingredients: {ingredients}
- Cuisine: {request.cuisine}
- Servings: {request.servings}
- Maximum cooking time: {request.cook_time_minutes} minutes
- Diet preference: {request.diet_preference}
- Spice level: {request.spice_level}
- Ingredients to avoid: {avoid}

Rules:
- Treat the natural language request as the primary instruction.
- Use optional structured inputs to fill missing details or override defaults.
- Prefer ingredients the user mentioned or provided.
- Do not use ingredients listed under "Ingredients to avoid".
- If extra ingredients are needed, mark them as optional.
- Keep the recipe realistic, beginner-friendly, and practical.
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