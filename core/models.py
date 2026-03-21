from datetime import datetime, timezone

from sqlalchemy import JSON, Column, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AuditSubmission(Base):
    __tablename__ = "submissions"

    # Use a real UUID or a clean serial ID
    id = Column(String, primary_key=True, index=True)
    business_name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Scoring Data
    score = Column(Integer)
    risk_level = Column(String)
    full_results = Column(JSON)  # Stores the 'failed' items and weights

    # Metadata
    status = Column(String, default="unpaid")  # unpaid, paid, failed
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    invoice_number = Column(String, unique=True)
