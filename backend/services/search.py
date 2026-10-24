import httpx

from backend.config import settings

TAVILY_URL = "https://api.tavily.com/search"


def _canonical(url: str) -> str:
    return url.split("?")[0].rstrip("/").lower()


class SearchClient:
    def __init__(self, api_key: str | None = None, timeout: int | None = None):
        self.api_key = api_key or settings.tavily_api_key
        self.timeout = timeout or settings.request_timeout

    def search(self, query: str, max_results: int, include_domains=None, exclude_domains=None):
        if not self.api_key:
            raise RuntimeError("Tavily API key is not configured.")
        payload = {
            "api_key": self.api_key,
            "query": query,
            "max_results": max_results,
            "include_domains": include_domains or [],
            "exclude_domains": exclude_domains or [],
        }
        with httpx.Client(timeout=self.timeout) as client:
            resp = client.post(TAVILY_URL, json=payload)
            resp.raise_for_status()
            data = resp.json()
        results = data.get("results", [])
        seen = set()
        out = []
        for r in results:
            url = r.get("url", "")
            key = _canonical(url)
            if key in seen:
                continue
            seen.add(key)
            out.append(
                {
                    "title": r.get("title", ""),
                    "url": url,
                    "domain": r.get("domain") or (url.split("/")[2] if "://" in url else ""),
                    "snippet": r.get("content", "") or r.get("snippet", ""),
                    "published_date": r.get("published_date"),
                }
            )
        return out
