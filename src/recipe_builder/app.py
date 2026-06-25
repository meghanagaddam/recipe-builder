from recipe_builder.models.recipe import RecipeRequest
from recipe_builder.services.recipe_generator import generate_recipe


def main():
    request = RecipeRequest(
        ingredients=["paneer", "spinach", "rice"],
        cuisine="Indian",
        servings=3,
        cook_time_minutes=30,
        diet_preference="High protein",
        spice_level="Mild",
        avoid_ingredients=["cream"],
    )

    recipe = generate_recipe(request)
    print(recipe)


if __name__ == "__main__":
    main()