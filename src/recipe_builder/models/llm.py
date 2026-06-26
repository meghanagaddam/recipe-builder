from pydantic import BaseModel


class LLMMetadata(BaseModel):
    provider: str
    model: str
    response_time_seconds: float
    temperature: float
    max_tokens: int

    input_tokens: int | None = None
    output_tokens: int | None = None
    total_tokens: int | None = None
    tokens_per_second: float | None = None


class LLMResponse(BaseModel):
    content: str
    metadata: LLMMetadata