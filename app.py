import os
import httpx
import streamlit as st

BACKEND = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="ResearchPilot AI", layout="wide")
st.title("ResearchPilot AI")
st.caption("Evidence-oriented web research assistant")

question = st.text_area("Research question", height=100)
depth = st.selectbox("Depth", ["quick", "standard", "deep"], index=1)
include = st.text_input("Include domains (comma-separated)", "")
exclude = st.text_input("Exclude domains (comma-separated)", "")

if st.button("Research"):
    if not question.strip():
        st.error("Question is required.")
    else:
        payload = {
            "question": question.strip(),
            "depth": depth,
            "include_domains": [d.strip() for d in include.split(",") if d.strip()],
            "exclude_domains": [d.strip() for d in exclude.split(",") if d.strip()],
        }
        with st.spinner("Researching..."):
            try:
                r = httpx.post(f"{BACKEND}/research", json=payload, timeout=120)
                r.raise_for_status()
                data = r.json()
            except Exception as e:
                st.error(f"Request failed: {e}")
                st.stop()
        st.subheader("Report")
        st.markdown(data["report_markdown"])
        st.subheader("Sources")
        for s in data["sources"]:
            st.markdown(f"- [{s['id']}] [{s['title']}]({s['url']}) — {s['domain']}")
        st.subheader("Caveats")
        for c in data["caveats"]:
            st.warning(c)
        st.download_button("Download Markdown", data["report_markdown"], file_name="report.md")

st.info(f"Backend URL: {BACKEND} — start the FastAPI backend (uvicorn backend.main:app) to run live research.")
