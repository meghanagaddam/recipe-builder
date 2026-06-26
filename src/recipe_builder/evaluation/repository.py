from pathlib import Path

from pydantic import ValidationError

from recipe_builder.models.evaluation import EvaluationRun


class EvaluationRepository:
    def __init__(self, log_file: Path) -> None:
        self.log_file = log_file

    def load_runs(self) -> list[EvaluationRun]:
        if not self.log_file.exists():
            return []

        runs: list[EvaluationRun] = []

        with self.log_file.open("r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                try:
                    runs.append(EvaluationRun.model_validate_json(line))
                except ValidationError:
                    continue

        return runs