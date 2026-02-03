# agent-k8s-demo

This repository demonstrates a Kubernetes-native AI agent implemented as a FastAPI service. The application is designed to run in a containerized, cloud-native environment and to integrate cleanly with external AI services through a single, structured invocation endpoint.

The project emphasizes real CI/CD behavior, multi-architecture container images, and secure secret handling. It is intentionally minimal in scope to focus on operational correctness, runtime safety, and production-ready integration patterns.

## Architecture (high level)

Client
  -> FastAPI AI Agent
      -> OpenAI API
  -> Kubernetes Service
      -> Pod (container)

## Key Technical Highlights

- Real multi-arch Docker builds (amd64 + arm64) using QEMU
- Clean OCI manifests (no unknown artifacts)
- Kubernetes-native secret injection
- Stateless AI agent design
- Proper local access via kubectl port-forward
- CI as the source of truth for runtime artifacts

## API Contract

POST /invoke

Minimal request:

```json
{
  "input": "string",
  "context": {
    "optional_key": "optional_value"
  }
}
```

Minimal response:

```json
{
  "output": "string",
  "model": "string",
  "latency_ms": 123.45
}
```

## Security Model

Secrets are never committed to the repository. API keys are injected at runtime via Kubernetes Secrets, keeping the codebase safe to be public while maintaining operational security.

## Local Development (minimal)

- Create a Kubernetes Secret that provides `OPENAI_API_KEY`.
- Deploy the manifests for the service and its dependencies.
- Access the service locally with `kubectl port-forward`.

## Scope & Next Steps

Out of scope for this repo: authentication, persistence, tool calling, ingress, and production hardening. These are deliberate omissions to keep the focus on the Kubernetes-native agent workflow and CI-managed artifacts.
