# ResearchPilot AI Implementation Plan

## Goal

Build the documented ResearchPilot AI application: FastAPI backend + Streamlit frontend + tests, using Tavily search and an NVIDIA Nemotron model via Nebius, with strict citation validation.

## Scope

Implement all modules listed in ARCHITECTURE.md/BUILD_PROMPT.md, plus config, schemas, services, export, tests, docs, and MIT license. No deployment claims until verified.

## Ordered Tasks

1. Verify provider docs (Nebius endpoint/auth/model ID; Tavily API) before coding; record chosen model and endpoint in config and README.
2. Scaffold project structure and dependencies (`requirements.txt`, `.env.example`, `.gitignore`).
3. Implement `backend/config.py` (env loading, validation, limits, timeouts).
4. Implement `backend/schemas.py` (request/response Pydantic models).
5. Implement `backend/services/search.py` (Tavily client, normalization, dedup by canonical URL, timeouts/errors).
6. Implement `backend/services/llm.py` (Nebius client, model ID from config, prompt with untrusted-source handling).
7. Implement `backend/services/research.py` (orchestration, evidence bounding, mode limits).
8. Implement `backend/services/verification.py` (source-ID validation, caveat generation, injection-safe handling).
9. Implement `backend/export.py` (Markdown export helpers).
10. Implement `backend/main.py` (FastAPI app, `/health`, `/research`, safe errors).
11. Implement `app.py` Streamlit UI (input, depth, filters, progress, report, sources, caveats, copy/download, demo mode).
12. Add tests (dedup, empty results, provider timeout/error, malformed model output, invalid source IDs, insufficient evidence, injection handling, export).
13. Write/update docs (README, HOW_TO_START, ARCHITECTURE, EVALUATION) to reflect actual implementation and model usage; add MIT LICENSE.
14. Run `pytest -q`, lint/typecheck if available; fix failures.

## Key Decisions

- Provider interfaces isolated for testability/mocking.
- Secrets only via env; never logged.
- Treat retrieved content as untrusted; ignore embedded instructions.
- Snippets are not full-page verification; disclose limitations.
- Citation IDs validated per run; invalid markers removed/flagged.

## Risks

- Model availability/endpoint may change; verify against official docs.
- Tavily rate limits/timeouts need handling.
- Prompt injection in source text.

## Validation

- `pytest -q` passes with mocked providers.
- `/health` returns status only.
- `/research` validates input and returns report/sources/caveats/model_id.
- Manual run with credentials verifies live search + inference.
- No secrets committed.

## Open Questions

- Exact Nebius model ID and endpoint to be confirmed from official docs during implementation.
- Whether to implement optional full-page extraction (default: snippets only, disclosed).

## Plan File

`/workspaces/ai-agents/.kilo/plans/1792827620213-researchpilot-build-plan.md`
