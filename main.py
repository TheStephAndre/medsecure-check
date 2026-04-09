import os

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

import core.models as models  # Ensure models are loaded
import core.wording as wording
from api.v1.endpoints import router as api_v1_router
from core.database import Base, engine  # New: Database imports
from core.ui import templates

# Initialize Database Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MedSecure-Check RaaS", version="2.0.0")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# --- HELPER FUNCTION ---
def get_lexicon(lang: str = "de-CH"):
    """Fetch the correct language dictionary from core.wording"""
    # Fallback to German if the requested language doesn't exist
    return wording.LEXICON.get(lang, wording.LEXICON["de-CH"])


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


# --- HOME ROUTE ---
@app.get("/", response_class=HTMLResponse)
async def index(request: Request, lang: str = "de-CH"):

    # Get the correct dictionary based on the URL parameter
    lex = get_lexicon(lang)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "current_lang": lang,
            "LANDING": lex["LANDING"],
            "PRODUCT": lex["PRODUCT"],
            "DISCLAIMERS": lex["DISCLAIMERS"],
        },
    )


# --- AUDIT ROUTE ---
@app.get("/audit", response_class=HTMLResponse, name="audit")
async def audit(request: Request, lang: str = "de-CH"):
    from core.scoring import QUESTIONS

    lex = get_lexicon(lang)

    return templates.TemplateResponse(
        "audit.html",
        {
            "request": request,
            "questions": QUESTIONS,
            "current_lang": lang,
            "AUDIT": lex["AUDIT"],
            "PRODUCT": lex["PRODUCT"],
            "DISCLAIMERS": lex["DISCLAIMERS"],
        },
    )
