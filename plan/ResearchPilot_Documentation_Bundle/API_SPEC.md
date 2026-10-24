# API Specification

This is the proposed API contract. Adjust it to match the
implementation.

## `GET /health`

Returns a basic health response without revealing secrets or provider
credentials.

Example:

``` json
{
  "status": "ok"
}
```

## `POST /research`

Accepts a research request.

Example request:

``` json
{
  "question": "What are the current approaches to reducing hallucinations in language models?",
  "depth": "standard",
  "include_domains": [],
  "exclude_domains": [],
  "date_range": null
}
```

Validation: - `question` must be non-empty and within a configured
maximum length. - `depth` must be one of `quick`, `standard`, or
`deep`. - Domain filters must be validated and bounded. - The server
must enforce request timeouts and source-count limits.

Example response:

``` json
{
  "question": "What are the current approaches to reducing hallucinations in language models?",
  "report_markdown": "# Research report\n...",
  "sources": [
    {
      "id": "S1",
      "title": "Example title returned by search",
      "url": "https://example.com/article",
      "domain": "example.com",
      "snippet": "Snippet returned by the provider"
    }
  ],
  "caveats": [
    "Some sources may be represented by search snippets rather than full-page text."
  ],
  "model_id": "configured-model-id"
}
```

The example values are illustrative, not real research findings or a
claim that this endpoint already exists.

## Error handling

Use safe, consistent responses for invalid input, missing configuration,
provider authentication failures, rate limits, timeouts, and unexpected
errors. Never include API keys or full secret-bearing environment values
in an error response.

## Source validation

Before returning a report, check every source marker against the source
IDs from that request. Unknown source IDs should be removed or flagged
and the report should be corrected or marked incomplete.
