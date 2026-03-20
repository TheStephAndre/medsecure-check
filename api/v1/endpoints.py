from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr
from typing import Dict
import uuid

# Professional Import Path from our new /core folder
from core.scoring import AuditEngine, QUESTIONS
import core.wording as wording

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# --- RaaS SCHEMA ---
class AuditSubmission(BaseModel):
    business_name: str
    email: EmailStr
    answers: Dict[str, str]

# --- API ENDPOINT (The RaaS Product) ---
@router.post("/assess")
async def api_assess(submission: AuditSubmission):
    """The core engine accessible via JSON for third-party integration."""
    engine = AuditEngine(submission.answers)
    results = engine.compute()
    return {
        "status": "success",
        "submission_id": str(uuid.uuid4())[:8],
        "results": results
    }

# --- WEB ENDPOINT (The UI Form) ---
@router.post("/submit", response_class=HTMLResponse)
async def web_submit(
    request: Request,
    business_name: str = Form(...),
    email: str = Form(...)
):
    """Handles traditional HTML form submissions from the website."""
    form_data = await request.form()
    # Filter only keys starting with 'q' for the scoring engine
    answers = {k: v for k, v in form_data.items() if k.startswith("q")}
    
    engine = AuditEngine(answers)
    results = engine.compute()
    
    return templates.TemplateResponse("result.html", {
        "request": request,
        "business_name": business_name,
        "results": results,
        "RESULT": wording.RESULT
    })
