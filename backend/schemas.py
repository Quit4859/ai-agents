import re
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator

MAX_DOMAINS = 20
MAX_DOMAIN_LENGTH = 253


class ResearchRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=500)
    depth: str = "standard"
    include_domains: List[str] = Field(default_factory=list, max_length=MAX_DOMAINS)
    exclude_domains: List[str] = Field(default_factory=list, max_length=MAX_DOMAINS)
    date_range: Optional[str] = None

    @field_validator("include_domains", "exclude_domains")
    @classmethod
    def _validate_domains(cls, value):
        cleaned = []
        for d in value or []:
            d = d.strip().lower()
            if not d:
                continue
            if len(d) > MAX_DOMAIN_LENGTH or not re.fullmatch(r"[a-z0-9.-]+", d):
                raise ValueError(f"Invalid domain: {d}")
            cleaned.append(d)
        return cleaned


class Source(BaseModel):
    id: str
    title: str
    url: str
    domain: str
    snippet: str = ""
    published_date: Optional[str] = None
    retrieval_method: str = "search_snippet"


class ResearchResponse(BaseModel):
    question: str
    report_markdown: str
    sources: List[Source]
    caveats: List[str]
    model_id: str
    search_provider: str = "tavily"
    created_at: Optional[str] = None
