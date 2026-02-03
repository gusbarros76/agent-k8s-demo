"""Agent logic for the demo API."""

from __future__ import annotations

import json
import os
import time

from openai import OpenAI

DEFAULT_MODEL = "gpt-4o-mini"


class MissingAPIKeyError(RuntimeError):
    pass


def run_agent(user_input: str) -> str:
    cleaned = user_input.strip()
    return f"agent_response: {cleaned}"


def invoke_agent(user_input: str, context: dict[str, str] | None) -> tuple[str, str, float]:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise MissingAPIKeyError("OPENAI_API_KEY not configured")

    client = OpenAI(api_key=api_key)
    message = _build_message(user_input, context or {})

    started = time.perf_counter()
    response = client.responses.create(
        model=DEFAULT_MODEL,
        input=message,
    )
    latency_ms = (time.perf_counter() - started) * 1000.0

    output_text = response.output_text or ""
    model = getattr(response, "model", DEFAULT_MODEL)
    return output_text, model, latency_ms


def _build_message(user_input: str, context: dict[str, str]) -> str:
    cleaned = user_input.strip()
    if not context:
        return cleaned
    context_json = json.dumps(context, ensure_ascii=True, separators=(",", ":"))
    return f"Context: {context_json}\nInput: {cleaned}"
