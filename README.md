# Agent API Demo

Minimal FastAPI service that exposes a fake "agent" API.

## Requirements
- Python 3.12
- uv

## Local setup
```bash
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
```

## Run the server
```bash
uv run uvicorn app.main:app --reload
```

## Example requests
```bash
curl http://127.0.0.1:8000/health
```

```bash
curl -X POST http://127.0.0.1:8000/run \
  -H "Content-Type: application/json" \
  -d '{"input":"hello"}'
```

## Run tests
```bash
uv run pytest
```

## Docker
Build the image:
```bash
docker build -t agent-api-demo .
```

Run the container:
```bash
docker run --rm -p 8000:8000 agent-api-demo
```
