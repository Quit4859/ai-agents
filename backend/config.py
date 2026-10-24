import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


def _int_env(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None or not raw.strip():
        return default
    try:
        return int(raw)
    except ValueError:
        return default


DEPTH_LIMITS = {
    "quick": _int_env("MAX_SOURCES_QUICK", 5),
    "standard": _int_env("MAX_SOURCES_STANDARD", 8),
    "deep": _int_env("MAX_SOURCES_DEEP", 12),
}


@dataclass
class Settings:
    nebius_api_key: str = os.getenv("NEBIUS_API_KEY", "")
    nebius_base_url: str = os.getenv("NEBIUS_BASE_URL", "https://api.studio.nebius.ai/v1")
    nebius_model_id: str = os.getenv("NEBIUS_MODEL_ID", "")
    tavily_api_key: str = os.getenv("TAVILY_API_KEY", "")
    backend_url: str = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
    max_question_length: int = _int_env("MAX_QUESTION_LENGTH", 500)
    request_timeout: int = _int_env("REQUEST_TIMEOUT_SECONDS", 30)


settings = Settings()


def validate_settings() -> list[str]:
    errors = []
    if not settings.nebius_api_key:
        errors.append("NEBIUS_API_KEY is not configured.")
    if not settings.nebius_model_id:
        errors.append("NEBIUS_MODEL_ID is not configured.")
    if not settings.tavily_api_key:
        errors.append("TAVILY_API_KEY is not configured.")
    return errors
