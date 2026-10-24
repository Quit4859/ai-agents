def to_markdown(response: dict) -> str:
    parts = [f"# Research report: {response['question']}", "", response["report_markdown"], "", "## Sources"]
    for s in response["sources"]:
        parts.append(f"- [{s.id if hasattr(s,'id') else s['id']}] {s.title if hasattr(s,'title') else s['title']} — {s.url if hasattr(s,'url') else s['url']}")
    if response.get("caveats"):
        parts.append("")
        parts.append("## Caveats")
        for c in response["caveats"]:
            parts.append(f"- {c}")
    return "\n".join(parts)
