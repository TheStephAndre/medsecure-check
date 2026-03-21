from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

import core.wording as wording
from api.v1.endpoints import router as api_v1_router
from core.ui import templates

app = FastAPI(title="MedSecure-Check RaaS", version="2.0.0")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")


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
    from core.scoring import QUESTIONS  # Import here to keep main clean

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
