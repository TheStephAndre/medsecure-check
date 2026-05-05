import os

from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

from api.v1.endpoints import router as api_v1_router
from core.database import Base, engine  # New: Database imports
from core.scoring import QUESTION_CONFIG
from core.ui import templates
from core.wording import get_lexicon

# Initialize Database Tables
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


# --- HOME ROUTE ---
@app.get("/", response_class=HTMLResponse)
async def index(request: Request, lang: str = "fr-CH"):

    # Get the correct dictionary based on the URL parameter
    lex = get_lexicon(lang)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "current_lang": lang,
            "lex": lex,
            "LANDING": lex["LANDING"],
            "PRODUCT": lex["PRODUCT"],
            "DISCLAIMERS": lex["DISCLAIMERS"],
        },
    )


# --- AUDIT ROUTE ---
@app.get("/audit", response_class=HTMLResponse, name="audit")
async def audit(request: Request, lang: str = "fr-CH"):

    # Get the localized text
    lex = get_lexicon(lang)

    # Combine them for the template
    # We create a list of questions that have both the ID and the localized text
    localized_questions = []
    for cfg in QUESTION_CONFIG:
        q_id = cfg["id"]
        localized_questions.append({"id": q_id, "text": lex["QUESTIONS"][q_id]["text"]})

    return templates.TemplateResponse(
        request=request,
        name="audit.html",
        context={
            "current_lang": lang,
            "questions": localized_questions,  # This was showing as 'undefined'
            "lex": lex,
            "AUDIT": lex["AUDIT"],
            "PRODUCT": lex["PRODUCT"],
            "DISCLAIMERS": lex["DISCLAIMERS"],
        },
    )
