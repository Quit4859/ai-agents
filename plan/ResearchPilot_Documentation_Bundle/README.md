# ResearchPilot AI

ResearchPilot AI is an evidence-oriented web research assistant. It
searches the web, organizes retrieved sources, asks an NVIDIA Nemotron
model served through Nebius to synthesize findings, and produces a
report with source references and uncertainty notes.

> **Status:** Project specification/starter documentation. Do not
> describe the application as deployed or functional until the
> implementation has been built and tested.

## Features planned

-   Web search through Tavily
-   Report synthesis using an NVIDIA open-source model through Nebius
    Token Factory or Nebius AI Cloud
-   Numbered source references and a visible source list
-   Cross-source conflict and uncertainty notes
-   Quick, Standard, and Deep research modes
-   Markdown report export
-   Streamlit UI, FastAPI backend, and automated tests

## Requirements

-   Python 3.11 or newer
-   A Nebius Token Factory account/API key and a currently available
    NVIDIA open model
-   A Tavily API key for live web search

Check the official provider documentation before configuring model IDs
or endpoints. Do not commit real API keys.

## Quick start

1.  Create and activate a virtual environment.
2.  Install dependencies from `requirements.txt` once the implementation
    has created it.
3.  Copy `.env.example` to `.env` and add your own credentials.
4.  Start the backend and frontend using the commands documented in
    `HOW_TO_START.md`.
5.  Open the local Streamlit URL printed in the terminal.

See [HOW_TO_START.md](HOW_TO_START.md) for the detailed setup checklist.

## How it works

1.  The user submits a research question.
2.  Tavily retrieves web search results.
3.  The backend deduplicates sources and prepares bounded evidence.
4.  Nemotron drafts a structured report grounded in those sources.
5.  Validation checks source IDs and highlights uncertainty or
    disagreement.
6.  The UI displays the report and links to the original sources.

The application must not fabricate citations. Search snippets are not
equivalent to full-page verification, and the UI should disclose when
full page content was not retrieved.

## Hackathon fit

**Suggested track:** Best Apps and Agents.

The submitted working version must actually run on Nebius Token Factory
or Nebius AI Cloud and use at least one NVIDIA open-source model.
Document the exact model, where inference occurs, and what role the
model plays. A mention in the README alone does not satisfy the
requirement.

## Environment variables

Use `.env.example` as the template. Keep secrets server-side and out of
source control.

## Testing

Run the test suite with:

``` bash
pytest -q
```

Tests should mock external services so they can run without live
credentials.

## Deployment checklist

-   [ ] Configure secrets in the hosting provider's secret manager
-   [ ] Verify the chosen NVIDIA model and Nebius endpoint
-   [ ] Verify Tavily search works
-   [ ] Run tests
-   [ ] Deploy backend and frontend
-   [ ] Test a live research question
-   [ ] Confirm all citations point to retrieved sources
-   [ ] Add the live demo URL to the hackathon submission
-   [ ] Record a public demo video of 3 minutes or less
-   [ ] Include an open-source license and setup instructions

## Limitations

AI-generated reports can contain errors. ResearchPilot should show
source links, disclose evidence gaps, and avoid claiming certainty when
sources are weak or contradictory. It is a research aid, not a
substitute for expert judgment.
