from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from api.v1.endpoints import router as api_v1_router
import core.wording as wording

app = FastAPI(title="MedSecure-Check RaaS", version="2.0.0")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Register our Modular Routes
app.include_router(api_v1_router, prefix="/api/v1")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "LANDING": wording.LANDING,
        "PRODUCT": wording.PRODUCT
    })

@app.get("/audit")
async def audit(request: Request):
    from core.scoring import QUESTIONS # Import here to keep main clean
    return templates.TemplateResponse("audit.html", {
        "request": request,
        "questions": QUESTIONS,
        "AUDIT": wording.AUDIT
    })
