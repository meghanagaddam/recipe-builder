from pydantic import BaseModel


class LLMMetadata(BaseModel):
    model: str
    response_time_seconds: float
    temperature: float
    max_tokens: int


class LLMResponse(BaseModel):
    content: str
    metadata: LLMMetadata