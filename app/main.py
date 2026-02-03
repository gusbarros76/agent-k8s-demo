from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.agent import MissingAPIKeyError, invoke_agent, run_agent
from app.models import InvokeRequest, InvokeResponse

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


@app.post("/invoke", response_model=InvokeResponse)
def invoke(payload: InvokeRequest) -> InvokeResponse | JSONResponse:
    try:
        output, model, latency_ms = invoke_agent(payload.input, payload.context)
    except MissingAPIKeyError as exc:
        return JSONResponse(status_code=500, content={"error": str(exc)})
    return InvokeResponse(output=output, model=model, latency_ms=latency_ms)
