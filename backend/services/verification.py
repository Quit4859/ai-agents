import json
import re

MARKER_RE = re.compile(r"\[S\d+\]")


REQUIRED_SECTIONS = [
    "Executive summary",
    "Key findings",
    "Evidence and supporting sources",
    "Conflicting evidence or caveats",
    "What remains uncertain",
    "Conclusion",
    "Sources",
]


def _normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def _find_markers(text):
    return set(MARKER_RE.findall(text))


def _build_cross_prompt(report: str, sources) -> str:
    src_block = "\n".join(
        f"[{s.id}] {s.title} - {s.url}\nSnippet: {s.snippet}" for s in sources
    )
    return (
        "You are a research evidence reviewer. Review the report against the "
        "provided sources and identify evidence-discipline issues:\n"
        "1. Claims supported by only one source (single_source).\n"
        "2. Conflicting evidence between sources (conflict).\n"
        "3. Unsupported or invented claims (unsupported).\n"
        "Respond with ONLY a JSON array of issues, each like "
        '{"type": "single_source"|"conflict"|"unsupported", "detail": "..."}. '
        "If no issues exist, respond with [].\n\n"
        f"Report:\n{report}\n\nSources:\n{src_block}"
    )


def _parse_cross_issues(raw: str) -> list:
    try:
        data = json.loads(raw)
    except Exception:
        return []
    issues = []
    if isinstance(data, dict):
        data = data.get("issues") or data.get("items") or []
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                issues.append({
                    "type": str(item.get("type") or "unsupported"),
                    "detail": str(item.get("detail") or item.get("description") or ""),
                })
            elif isinstance(item, str) and item.strip():
                issues.append({"type": "unsupported", "detail": item.strip()})
    return [i for i in issues if i.get("detail")]


def cross_check(report: str, sources, llm_client) -> list:
    if not sources:
        return []
    raw = llm_client.complete(_build_cross_prompt(report, sources))
    issues = _parse_cross_issues(raw)
    caveats = []
    for issue in issues:
        caveats.append(f"Cross-check found {issue.get('type')}: {issue.get('detail')}")
    if not issues:
        caveats.append("Cross-check found no single-source claims or conflicts.")
    return caveats


def validate_report_sections(report: str) -> list:
    text = _normalize(report)
    missing = []
    for section in REQUIRED_SECTIONS:
        if _normalize(section) not in text:
            missing.append(section)
    return missing


def validate_report(report: str, valid_ids: set[str]):
    markers = _find_markers(report)
    valid = {v.strip("[]") for v in valid_ids}
    invalid = [m for m in markers if m.strip("[]") not in valid]
    caveats = []
    if invalid:
        for m in invalid:
            report = report.replace(m, "")
        caveats.append(f"Removed unknown source markers: {', '.join(sorted(invalid))}.")
    if "conflict" not in report.lower() and "caveat" not in report.lower() and "uncertain" not in report.lower():
        caveats.append("Report did not explicitly discuss conflicts or uncertainty.")
    missing_sections = validate_report_sections(report)
    if missing_sections:
        caveats.append(f"Report was missing expected sections: {', '.join(missing_sections)}.")
    return report, caveats
