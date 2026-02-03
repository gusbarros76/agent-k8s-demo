from fastapi import FastAPI
from pydantic import BaseModel

from app.agent import run_agent

app = FastAPI(title="Agent API Demo")


class RunRequest(BaseModel):
    input: str


class RunResponse(BaseModel):
    output: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/run", response_model=RunResponse)
def run(payload: RunRequest) -> dict[str, str]:
    output = run_agent(payload.input)
    return {"output": output}
