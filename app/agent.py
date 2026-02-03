"""Deterministic agent logic for the demo API."""


def run_agent(user_input: str) -> str:
    cleaned = user_input.strip()
    return f"agent_response: {cleaned}"
