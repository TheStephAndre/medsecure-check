from datetime import datetime, timezone

from sqlalchemy import JSON, Boolean, Column, DateTime, Integer, String

from .database import Base


class AuditSubmission(Base):
    __tablename__ = "submissions"

    id = Column(String, primary_key=True, index=True)  # Our 16-char ID
    business_name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    score = Column(Integer)
    risk_level = Column(String)
    failed_items = Column(JSON)  # Stores the list of security gaps

    is_paid = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
