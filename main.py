import os

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

import core.models as models  # New: Ensure models are loaded
import core.wording as wording
from api.v1.endpoints import router as api_v1_router
from core.database import Base, engine  # New: Database imports
from core.ui import templates

# Initialize Database Tables (Automatic Migration for MVP)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MedSecure-Check RaaS", version="2.0.0")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# --- FAVICON FIX ---
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """
    Directs browsers looking for /favicon.ico to the static folder.
    This stops the 404 errors in the terminal.
    """
    file_path = os.path.join("static", "favicon.ico")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return Response(status_code=204)  # Fallback if file is missing


# Register our Modular Routes
app.include_router(api_v1_router, prefix="/api/v1")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "LANDING": wording.LANDING,
            "PRODUCT": wording.PRODUCT,
            "DISCLAIMERS": wording.DISCLAIMERS,
        },
    )


@app.get("/audit")
async def audit(request: Request):
    from core.scoring import QUESTIONS

    return templates.TemplateResponse(
        "audit.html",
        {
            "request": request,
            "questions": QUESTIONS,
            "AUDIT": wording.AUDIT,
            "PRODUCT": wording.PRODUCT,
            "DISCLAIMERS": wording.DISCLAIMERS,
        },
    )
