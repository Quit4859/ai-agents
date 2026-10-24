import re


def _find_markers(text):
    return set(re.findall(r"\[S\d+\]", text))


def validate_report(report: str, valid_ids: set[str]):
    markers = _find_markers(report)
    invalid = [m for m in markers if m.strip("[]") not in {v.strip("[]") for v in valid_ids}]
    caveats = []
    if invalid:
        for m in invalid:
            report = report.replace(m, "")
        caveats.append(f"Removed unknown source markers: {', '.join(invalid)}.")
    # flag single-source claims heuristic: if report has no conflict mention
    if "conflict" not in report.lower() and "caveat" not in report.lower() and "uncertain" not in report.lower():
        caveats.append("Report did not explicitly discuss conflicts or uncertainty.")
    return report, caveats
