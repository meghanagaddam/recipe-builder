import pandas as pd

from recipe_builder.models.evaluation import EvaluationRun


def evaluation_runs_to_dataframe(runs: list[EvaluationRun]) -> pd.DataFrame:
    rows: list[dict] = []

    for run in runs:
        rows.append(
            {
                "run_id": str(run.run_id),
                "created_at": run.created_at,
                "prompt_version": run.prompt_version,
                "ingredients": run.request.ingredients,
                "provider": run.metadata.provider,
                "model": run.metadata.model,
                "temperature": run.metadata.temperature,
                "max_tokens": run.metadata.max_tokens,
                "response_time_seconds": run.metadata.response_time_seconds,
                "input_tokens": run.metadata.input_tokens,
                "output_tokens": run.metadata.output_tokens,
                "total_tokens": run.metadata.total_tokens,
                "tokens_per_second": run.metadata.tokens_per_second,
            }
        )

    df = pd.DataFrame(rows)

    if df.empty:
        return df

    df["output_token_ratio"] = df["output_tokens"] / df["total_tokens"]
    df["seconds_per_output_token"] = (
        df["response_time_seconds"] / df["output_tokens"]
    )

    return df