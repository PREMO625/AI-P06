from pathlib import Path
from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from backend import HospitalExpertSystem


BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
DURATION_OPTIONS = ["< 24 hours", "1-2 days", "3-7 days", "> 1 week"]

engine = HospitalExpertSystem()
app = FastAPI(title="Hospital and Medical Facilities Expert System")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class DiagnoseRequest(BaseModel):
    symptoms: List[str] = Field(default_factory=list)
    age: int = Field(ge=1, le=100)
    pain_scale: int = Field(ge=0, le=10)
    duration: str


@app.get("/")
def get_home() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/meta")
def get_meta() -> dict:
    return {
        "symptoms": engine.list_symptoms(),
        "durations": DURATION_OPTIONS,
    }


@app.post("/api/diagnose")
def diagnose(payload: DiagnoseRequest) -> dict:
    if payload.duration not in DURATION_OPTIONS:
        raise HTTPException(status_code=400, detail="Invalid duration option")

    return engine.evaluate(
        selected_symptoms=set(payload.symptoms),
        age=payload.age,
        pain_scale=payload.pain_scale,
        symptom_duration=payload.duration,
    )


@app.get("/__debug")
def debug_status() -> dict:
    return {
        "mode": "fastapi-static",
        "static_dir_exists": STATIC_DIR.exists(),
        "symptom_count": len(engine.list_symptoms()),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)





