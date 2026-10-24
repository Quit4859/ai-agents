import httpx

from backend.config import settings


class ContentExtractor:
    """Interface for retrieving full page content for a source."""

    def extract(self, source: dict) -> str:
        return ""


class TavilyContentExtractor(ContentExtractor):
    """Retrieves full page content through Tavily; falls back to the snippet."""

    def __init__(self, api_key: str | None = None, timeout: int | None = None):
        self.api_key = api_key or settings.tavily_api_key
        self.timeout = timeout or settings.request_timeout

    def extract(self, source: dict) -> str:
        snippet = source.get("snippet") or ""
        url = source.get("url") or ""
        if not self.api_key or not url:
            return snippet
        try:
            resp = httpx.post(
                "https://api.tavily.com/extract",
                json={"urls": [url], "query": source.get("query") or "", "extract_depth": "basic"},
                timeout=self.timeout,
                headers={"Authorization": f"Bearer {self.api_key}"},
            )
            resp.raise_for_status()
            data = resp.json()
            for r in data.get("results") or []:
                if r.get("url") == url:
                    return r.get("raw_content") or snippet
        except Exception:
            return snippet
        return snippet
