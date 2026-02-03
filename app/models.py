from __future__ import annotations

from pydantic import BaseModel, Field


class InvokeRequest(BaseModel):
    input: str
    context: dict[str, str] = Field(default_factory=dict)


class InvokeResponse(BaseModel):
    output: str
    model: str
    latency_ms: float
