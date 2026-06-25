from ollama import chat

def generate_recipe():
    prompt = """
    You are a professional recipe assistant.

    Create a recipe using:
    - Ingredients: paneer, spinach, rice
    - Cuisine: Indian
    - Servings: 3
    - Cooking time: under 30 minutes
    - Spice level: mild

    Return:
    1. Recipe name
    2. Ingredients with quantities
    3. Step-by-step instructions
    4. Cooking time
    5. Nutrition estimate
    6. Substitutions
    """

    response = chat(
        model="qwen3:8b",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response["message"]["content"]

if __name__ == "__main__":
    recipe = generate_recipe()
    print(recipe)