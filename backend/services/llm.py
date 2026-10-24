import httpx

from backend.config import settings


class LLMClient:
    def __init__(self, api_key=None, base_url=None, model_id=None, timeout=None):
        self.api_key = api_key or settings.nebius_api_key
        self.base_url = (base_url or settings.nebius_base_url).rstrip("/")
        self.model_id = model_id or settings.nebius_model_id
        self.timeout = timeout or settings.request_timeout

    def complete(self, prompt: str) -> str:
        if not self.api_key:
            raise RuntimeError("Nebius API key is not configured.")
        if not self.model_id:
            raise RuntimeError("Nebius model ID is not configured.")
        url = f"{self.base_url}/chat/completions"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        body = {
            "model": self.model_id,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
        }
        with httpx.Client(timeout=self.timeout) as client:
            resp = client.post(url, json=body, headers=headers)
            resp.raise_for_status()
            data = resp.json()
        return data["choices"][0]["message"]["content"]
