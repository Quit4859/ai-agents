# Evaluation and Hackathon Demo Plan

## What the judges should see

1.  **Problem:** Research across many web pages is slow, and it is hard
    to compare claims or track evidence.
2.  **Live workflow:** Enter a real question and launch research.
3.  **Visible sources:** Show retrieved source titles and clickable
    URLs.
4.  **Nemotron usage:** Explain which NVIDIA open-source model is
    configured, that inference runs through Nebius, and which workflow
    steps use it.
5.  **Evidence discipline:** Show a conflict, caveat, or uncertainty
    note rather than presenting every generated statement as certain.
6.  **Useful output:** Export the report as Markdown.
7.  **Reliability:** Demonstrate an error state or test result briefly.

## Suggested three-minute video

-   0:00--0:20 --- State the problem and target users.
-   0:20--0:45 --- Introduce ResearchPilot and its core workflow.
-   0:45--1:35 --- Run a live question; show search results and report
    generation.
-   1:35--2:10 --- Show citations, conflicting evidence, and uncertainty
    notes.
-   2:10--2:35 --- Explain the Nebius Token Factory and NVIDIA model
    integration.
-   2:35--2:50 --- Show export and repository setup instructions.
-   2:50--3:00 --- Summarize impact and what makes the approach useful.

Record the real working application. Do not use mock data while implying
it is live.

## Acceptance checklist

-   [ ] Working app deployed and accessible
-   [ ] Runtime inference uses Nebius
-   [ ] At least one NVIDIA open-source model is actually used
-   [ ] Live search works
-   [ ] Citations map to sources returned in the same run
-   [ ] Conflicting or insufficient evidence is disclosed
-   [ ] Tests pass
-   [ ] Public repository contains setup instructions
-   [ ] Open-source license is visible at repository root
-   [ ] Demo video is public and at most three minutes
-   [ ] README accurately describes the implementation

## Honest limitations to mention

-   Search coverage depends on the search provider and query.
-   Snippets can omit context; full-page extraction may fail.
-   A source supporting a claim does not automatically make that claim
    true.
-   Automated cross-checking can miss subtle contradictions.
-   Model and provider availability may change; verify configuration
    before judging.
