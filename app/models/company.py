"""Company model definitions."""

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.db import Base


class Company(Base):
    """Model for storing company records."""

    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    company_code = Column(String, nullable=False, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
