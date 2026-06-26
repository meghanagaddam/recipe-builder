from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from recipe_builder.models.llm import LLMMetadata
from recipe_builder.models.recipe import RecipeRequest


class EvaluationRun(BaseModel):
    run_id: UUID
    timestamp: datetime
    prompt_version: str
    request: RecipeRequest
    metadata: LLMMetadata
    output_char_count: int = Field(ge=0)
    quality_score: int | None = Field(default=None, ge=1, le=5)
    notes: str = ""