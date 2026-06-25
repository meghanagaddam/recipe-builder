from pydantic import BaseModel, Field


class RecipeRequest(BaseModel):
    ingredients: list[str] = Field(..., min_length=1)
    cuisine: str = "Any"
    servings: int = Field(default=2, ge=1, le=10)
    cook_time_minutes: int = Field(default=30, ge=5, le=180)
    diet_preference: str = "None"
    spice_level: str = "Medium"
    avoid_ingredients: list[str] = []