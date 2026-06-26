import streamlit as st

from recipe_builder.models.recipe import RecipeRequest
from recipe_builder.services.recipe_generator import generate_recipe


def parse_comma_separated_text(text: str) -> list[str]:
    return [item.strip() for item in text.split(",") if item.strip()]


def main():
    st.set_page_config(
        page_title="AI Recipe Builder",
        page_icon="🍲",
        layout="centered",
    )

    st.title("🍲 AI Recipe Builder")
    st.write("Describe what you want to cook, and optionally refine it with filters.")

    user_request = st.text_area(
        "What would you like to cook?",
        placeholder="Example: I have paneer, spinach, and rice. Make something quick, healthy, and Indian-style.",
        height=120,
    )

    with st.expander("Optional filters"):
        ingredients_text = st.text_input(
            "Available ingredients",
            placeholder="Example: paneer, spinach, rice",
        )

        cuisine = st.selectbox(
            "Cuisine",
            ["Any", "Indian", "Italian", "Mexican", "Chinese", "Mediterranean", "American"],
        )

        diet_preference = st.selectbox(
            "Diet preference",
            ["None", "Vegetarian", "Vegan", "High protein", "Low carb", "Kid friendly"],
        )

        servings = st.slider("Servings", min_value=1, max_value=10, value=2)

        cook_time_minutes = st.slider(
            "Maximum cooking time",
            min_value=5,
            max_value=120,
            value=30,
            step=5,
        )

        spice_level = st.selectbox(
            "Spice level",
            ["Mild", "Medium", "Spicy"],
        )

        avoid_text = st.text_input(
            "Ingredients to avoid",
            placeholder="Example: cream, peanuts, eggs",
        )

    if st.button("Generate Recipe"):
        ingredients = parse_comma_separated_text(ingredients_text)
        avoid_ingredients = parse_comma_separated_text(avoid_text)

        if not user_request.strip() and not ingredients:
            st.error("Please describe what you want to cook or enter at least one ingredient.")
            return

        request = RecipeRequest(
            user_request=user_request.strip(),
            ingredients=ingredients,
            cuisine=cuisine,
            servings=servings,
            cook_time_minutes=cook_time_minutes,
            diet_preference=diet_preference,
            spice_level=spice_level,
            avoid_ingredients=avoid_ingredients,
        )

        with st.spinner("Generating your recipe..."):
            recipe = generate_recipe(request)

        st.subheader("Generated Recipe")
        st.write(recipe)


if __name__ == "__main__":
    main()