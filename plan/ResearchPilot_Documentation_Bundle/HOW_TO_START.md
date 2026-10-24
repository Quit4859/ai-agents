# How to Start ResearchPilot AI

This document is the setup plan for a fresh local development
environment.

## 1. Install prerequisites

Install Python 3.11+ and Git. Verify:

``` bash
python --version
git --version
```

On some systems, use `python3` instead of `python`.

## 2. Get the project files

Place the generated application code in a project directory. The
documentation bundle alone is not the running application; use
`BUILD_PROMPT.md` with your coding agent to generate the code.

## 3. Create a virtual environment

### macOS/Linux

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell

``` powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
```

## 4. Install dependencies

After the implementation creates `requirements.txt`, run:

``` bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Configure API credentials

Copy `.env.example` to `.env`. Add credentials from your own provider
accounts. Never commit `.env`.

Required configuration should include: - Nebius Token Factory API key -
Verified NVIDIA model identifier supported by your account - Tavily API
key - Backend URL if the frontend and backend run separately

Use the current official Nebius documentation to verify the endpoint,
authentication format, and model identifier. Do not copy example
credentials from tutorials.

## 6. Start the app

The exact commands depend on the generated implementation. For the
recommended layout, start the API in one terminal:

``` bash
uvicorn backend.main:app --reload
```

Then start Streamlit in another terminal:

``` bash
streamlit run app.py
```

If the implementation uses a different entry point, follow the commands
in its updated README. Open the local Streamlit URL shown in the
terminal.

## 7. Verify it works

1.  Open the app.
2.  Submit a simple research question.
3.  Confirm that live source links appear.
4.  Confirm the report uses source markers that match the source list.
5.  Check that uncertainty and conflicting evidence are disclosed.
6.  Download the Markdown report.
7.  Test the app with missing credentials and confirm it displays a
    useful error without exposing secrets.

## 8. Run tests

``` bash
pytest -q
```

Use mocked provider clients for tests so the suite does not require paid
API calls.

## Troubleshooting

-   **Missing API key:** Check `.env` variable names and restart the
    app.
-   **Invalid model ID:** Verify the model is currently available to
    your Nebius account.
-   **Provider authentication error:** Check credentials and the
    provider's current API documentation.
-   **No search results:** Try a more specific query and verify Tavily
    configuration.
-   **Frontend cannot reach API:** Confirm the backend is running and
    the configured backend URL is correct.
-   **Slow requests:** Reduce research depth or source count; add
    provider timeouts.
-   **Unexpected citations:** Ensure source IDs are validated against
    the results from the current run.

## Before submission

Run tests, verify live inference, deploy a working demo, add an
open-source license, and record a public demo video of three minutes or
less. Do not claim any step is complete until verified.
