import os
from io import BytesIO

from weasyprint import HTML

import core.wording as wording
from core.ui import templates


def generate_pdf(template_name: str, audit_record, company_name: str, iban: str):
    """
    Generic PDF generator for Reports and Invoices.
    Maps SQLAlchemy model fields to Template expectations.
    """
    # 1. Prepare the 'submission' object as the templates expect it
    # We map 'score' -> 'assessment' and 'failed_items' -> 'failed'
    submission_data = {
        "id": audit_record.id,
        "business_name": audit_record.business_name,
        "assessment": audit_record.score,
        "risk_level": audit_record.risk_level,
        "failed": audit_record.failed_items,
        "created_at_human": audit_record.created_at.strftime("%d.%m.%Y"),
        "invoice_number": f"RE-{audit_record.id[:8].upper()}",
    }

    # 2. Context for Jinja2
    context = {
        "submission": submission_data,
        "company": company_name,
        "IBAN": iban,
        "REPORT": wording.REPORT,
        "REPORT_PDF": wording.REPORT_PDF,
        "RISK_LEVELS": wording.RISK_LEVELS,
        "PRODUCT": wording.PRODUCT,
    }

    # 3. Render HTML
    template = templates.get_template(template_name)
    html_out = template.render(context)

    # 4. Generate PDF
    pdf_file = BytesIO()  # Save data in the RAM
    HTML(string=html_out).write_pdf(pdf_file)
    pdf_file.seek(0)
    return pdf_file
