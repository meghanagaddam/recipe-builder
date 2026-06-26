import pandas as pd

from recipe_builder.evaluation.metrics import evaluation_runs_to_dataframe
from recipe_builder.evaluation.repository import EvaluationRepository


class EvaluationService:
    def __init__(self, repository: EvaluationRepository) -> None:
        self.repository = repository

    def load_runs_dataframe(self) -> pd.DataFrame:
        runs = self.repository.load_runs()
        return evaluation_runs_to_dataframe(runs)