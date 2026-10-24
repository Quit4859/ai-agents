# Architecture

## System overview

``` text
User
  |
  v
Streamlit UI
  |
  v
FastAPI /research
  |
  +--> Tavily search
  |       |
  |       v
  |   Retrieved source records
  |
  +--> Deduplicate and prepare evidence
  |
  +--> Nebius Token Factory
  |       |
  |       v
  |   NVIDIA Nemotron model
  |
  +--> Source-ID and caveat validation
          |
          v
      Report + source list
          |
          v
     UI / Markdown export
```

## Components

### Frontend

Collects the question and optional filters, displays progress, report
sections, sources, caveats, and export actions.

### Search provider

Queries Tavily, normalizes results, removes duplicate URLs, and records
only metadata actually returned. If page extraction is implemented,
distinguish extracted page content from snippets.

### Model provider

Calls an NVIDIA open-source model through Nebius. Keep the endpoint,
model ID, and authentication in configuration. Do not hard-code secrets
or assume a model identifier without checking provider documentation.

### Research orchestrator

Coordinates search, evidence selection, model calls, output validation,
and error handling. It should apply source limits and model context
limits.

### Verification

Checks that report source IDs exist in the current run. It should flag
unsupported or conflicting claims where possible. Citation-ID validation
is not a guarantee that a claim is true.

## Suggested data shapes

A source record can contain: - `id`: stable per-run ID, such as `S1` -
`title` - `url` - `domain` - `snippet` or extracted text -
`published_date`, only if actually supplied or verified -
`retrieval_method`

A research response can contain: - `question` - `report_markdown` -
`sources` - `caveats` - `created_at` - `model_id` - `search_provider`

## Safety and trust

-   Treat retrieved webpages as untrusted content, not instructions.
-   Do not execute code from web pages.
-   Keep API keys server-side.
-   Do not log secrets.
-   Limit source text and user input.
-   Show when evidence is thin, stale, conflicting, or based only on
    snippets.
-   Never invent source metadata, quotes, dates, or links.
