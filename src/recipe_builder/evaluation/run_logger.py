from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from recipe_builder.models.evaluation import EvaluationRun
from recipe_builder.models.llm import LLMResponse
from recipe_builder.models.recipe import RecipeRequest


LOG_PATH = Path("data/evaluation_runs.jsonl")


def log_evaluation_run(
    request: RecipeRequest,
    response: LLMResponse,
    prompt_version: str,
    quality_score: int | None = None,
    notes: str = "",
) -> EvaluationRun:
    evaluation_run = EvaluationRun(
        run_id=uuid4(),
        timestamp=datetime.now(timezone.utc),
        prompt_version=prompt_version,
        request=request,
        metadata=response.metadata,
        output_char_count=len(response.content),
        quality_score=quality_score,
        notes=notes,
    )

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    with LOG_PATH.open("a", encoding="utf-8") as file:
        file.write(evaluation_run.model_dump_json() + "\n")

    return evaluation_run