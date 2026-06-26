import streamlit as st

from recipe_builder.models.recipe import RecipeRequest
from recipe_builder.services.recipe_generator import generate_recipe
from recipe_builder.config import DEFAULT_LLM_PROVIDER, DEFAULT_MODEL
from recipe_builder.services.llm.factory import LLMFactory
from recipe_builder.evaluation.run_logger import log_evaluation_run


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

    with st.sidebar:
        st.header("LLM Settings")

        provider = st.selectbox(
            "Provider",
            ["ollama"],
            index=0,
        )

        model = st.selectbox(
            "Model",
            ["qwen3:8b", "llama3.1:8b", "gemma3:4b"],
            index=0,
        )

        prompt_version = st.selectbox(
            "Prompt Version",
            ["recipe_v1", "recipe_v2"],
            index=0,
        )

        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.5,
            value=0.5,
            step=0.1,
        )

        max_tokens = st.slider(
            "Max output tokens",
            min_value=300,
            max_value=3000,
            value=1800,
            step=100,
        )

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
            llm = LLMFactory.create(
            provider=provider,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            )

            result = generate_recipe(
                request=request,
                llm=llm,
                prompt_version=prompt_version,
            )

            evaluation_run = log_evaluation_run(
                request=request,
                response=result,
                prompt_version=prompt_version,
            )

        st.success(
            f"Generated using {result.metadata.model} "
            f"in {result.metadata.response_time_seconds} seconds"
        )

        with st.expander("LLM Metrics"):
            st.write(f"Model: {result.metadata.model}")
            st.write(f"Response time: {result.metadata.response_time_seconds} seconds")
            st.write(f"Temperature: {result.metadata.temperature}")
            st.write(f"Max output tokens: {result.metadata.max_tokens}")
            st.write(f"Prompt version: {prompt_version}")
            st.write(f"Provider: {provider}")
            st.write(f"Run ID: {evaluation_run.run_id}")
            st.write(f"Input tokens: {result.metadata.input_tokens}")
            st.write(f"Output tokens: {result.metadata.output_tokens}")
            st.write(f"Total tokens: {result.metadata.total_tokens}")
            st.write(f"Tokens/sec: {result.metadata.tokens_per_second}")

        st.subheader("Generated Recipe")
        st.write(result.content)


if __name__ == "__main__":
    main()