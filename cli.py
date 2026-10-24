import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.config import settings
from backend.schemas import ResearchRequest
from backend.services.llm import LLMClient
from backend.services.providers import PROVIDERS
from backend.services.research import run_research
from backend.services.search import SearchClient


def main():
    parser = argparse.ArgumentParser(description="ResearchPilot CLI")
    parser.add_argument("--provider", choices=list(PROVIDERS), default="nebius")
    parser.add_argument("--api-key", default=None)
    parser.add_argument("--model", default=None)
    parser.add_argument("--question", required=True)
    parser.add_argument("--depth", choices=["quick", "standard", "deep"], default="standard")
    args = parser.parse_args()

    info = PROVIDERS[args.provider]
    api_key = args.api_key or os.getenv(info["env"], "")
    model = args.model or info["default_model"]
    base_url = info["base_url"]

    req = ResearchRequest(question=args.question, depth=args.depth)
    llm = LLMClient(api_key=api_key, base_url=base_url, model_id=model)
    search = SearchClient()
    result = run_research(req, search_client=search, llm_client=llm)
    print(result["report_markdown"])
    print("\n--- Sources ---")
    for s in result["sources"]:
        print(f"[{s.id}] {s.title} - {s.url}")


if __name__ == "__main__":
    main()
