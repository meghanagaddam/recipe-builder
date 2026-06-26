import streamlit as st

from recipe_builder.config import EVALUATION_LOG_FILE
from recipe_builder.evaluation.repository import EvaluationRepository
from recipe_builder.evaluation.service import EvaluationService


st.set_page_config(
    page_title="Evaluation Lab",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Evaluation Lab")
st.caption("Compare prompt versions, model settings, latency, and token usage across recipe generation runs.")

repository = EvaluationRepository(EVALUATION_LOG_FILE)
service = EvaluationService(repository)

df = service.load_runs_dataframe()

if df.empty:
    st.info("No evaluation runs found yet.")
    st.stop()

st.sidebar.header("Filters")

selected_models = st.sidebar.multiselect(
    "Model",
    options=sorted(df["model"].dropna().unique()),
    default=sorted(df["model"].dropna().unique()),
)

selected_prompt_versions = st.sidebar.multiselect(
    "Prompt Version",
    options=sorted(df["prompt_version"].dropna().unique()),
    default=sorted(df["prompt_version"].dropna().unique()),
)

selected_temperatures = st.sidebar.multiselect(
    "Temperature",
    options=sorted(df["temperature"].dropna().unique()),
    default=sorted(df["temperature"].dropna().unique()),
)

filtered_df = df[
    (df["model"].isin(selected_models))
    & (df["prompt_version"].isin(selected_prompt_versions))
    & (df["temperature"].isin(selected_temperatures))
]

if filtered_df.empty:
    st.warning("No runs match the selected filters.")
    st.stop()

def get_mode_value(df, column: str) -> str:
    mode_values = df[column].dropna().mode()

    if mode_values.empty:
        return "N/A"

    return str(mode_values.iloc[0])


st.subheader("Summary")

total_runs = len(filtered_df)
avg_response_time = filtered_df["response_time_seconds"].mean()
avg_output_tokens = filtered_df["output_tokens"].mean()
avg_tokens_per_second = filtered_df["tokens_per_second"].mean()

most_used_model = get_mode_value(filtered_df, "model")
most_used_prompt = get_mode_value(filtered_df, "prompt_version")

col1, col2, col3 = st.columns(3)

col1.metric("Total Runs", total_runs)
col2.metric("Avg Latency", f"{avg_response_time:.2f}s")
col3.metric("Avg Throughput", f"{avg_tokens_per_second:.2f} tok/s")

col4, col5, col6 = st.columns(3)

col4.metric("Avg Output Length", f"{avg_output_tokens:.0f} tokens")
col5.metric("Most Used Model", most_used_model)
col6.metric("Most Used Prompt", most_used_prompt)

st.subheader("Evaluation Runs")
st.dataframe(filtered_df, use_container_width=True)