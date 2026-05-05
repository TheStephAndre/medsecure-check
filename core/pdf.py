from io import BytesIO

from weasyprint import HTML

from core.ui import templates


def generate_pdf(
    template_name: str, audit_record, lexicon, company_name: str, **kwargs
):
    """
    Generic PDF generator for Reports and Invoices.
    Maps SQLAlchemy model fields to Template expectations.
    """
    # 1. Prepare the 'submission' object as the templates expect it
    # We map 'score' -> 'assessment' and 'failed_items' -> 'failed'
    submission_data = {
        "id": str(audit_record.id),
        "business_name": str(audit_record.business_name),
        "assessment": int(audit_record.score) if audit_record.score else 0,
        "risk_level": str(audit_record.risk_level),
        "failed": audit_record.failed_items,  # JSON list
        "created_at_human": audit_record.created_at.strftime("%d.%m.%Y"),
        "invoice_number": f"RE-{str(audit_record.id)[:8].upper()}",
        # Ensure the  audit_record has a pillar_scores attribute (JSON/Dict)
        "pillar_scores": (
            audit_record.pillar_scores if hasattr(audit_record, "pillar_scores") else {}
        ),
    }

    # 2. Context for Jinja2
    context = {
        "submission": submission_data,
        "company": company_name,
        "lexicon": lexicon,
        "PRODUCT": lexicon.get("PRODUCT"),
        "RESULT": lexicon.get("RESULT"),
        "RISK_LEVELS": lexicon.get("RISK_LEVELS"),
        "REPORT": lexicon.get("REPORT"),
        "REPORT_PDF": lexicon.get("REPORT_PDF"),
        "DISCLAIMERS": lexicon.get("DISCLAIMERS"),
        "INVOICE": lexicon.get("INVOICE"),
        **kwargs,  # Captures anything else like IBAN for invoices
    }

    # This merges extra stuff (like IBAN) into the context IF it exists
    context.update(kwargs)

    # 3. Render HTML
    template = templates.get_template(template_name)
    html_out = template.render(context)

    # 4. Generate PDF(WeasyPrint)
    pdf_file = BytesIO()  # Save data in the RAM
    # base_url allows WeasyPrint to find images/CSS in your static folder
    HTML(string=html_out).write_pdf(pdf_file, presentational_hints=True)
    pdf_file.seek(0)
    return pdf_file
