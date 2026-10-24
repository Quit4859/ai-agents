from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.config import settings, validate_settings
from backend.schemas import ResearchRequest, ResearchResponse
from backend.services.research import run_research

app = FastAPI(title="ResearchPilot AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/research", response_model=ResearchResponse)
def research(req: ResearchRequest):
    if req.depth not in ("quick", "standard", "deep"):
        raise HTTPException(status_code=422, detail="depth must be quick, standard, or deep")
    errors = validate_settings()
    if errors:
        raise HTTPException(status_code=503, detail="; ".join(errors))
    try:
        result = run_research(req)
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
    return ResearchResponse(**result)
