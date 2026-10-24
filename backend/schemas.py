from typing import List, Optional

from pydantic import BaseModel, Field


class ResearchRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=500)
    depth: str = "standard"
    include_domains: List[str] = Field(default_factory=list)
    exclude_domains: List[str] = Field(default_factory=list)
    date_range: Optional[str] = None


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
