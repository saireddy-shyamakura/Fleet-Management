"""User model and role enum definitions."""

import enum
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String

from app.db import Base


class UserRole(enum.Enum):
    """Supported user roles for access control."""

    ADMIN = "admin"
    DRIVER = "driver"
    SUPERADMIN = "superadmin"


class User(Base):
    """Model for storing application users."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)

    company_id = Column(Integer, ForeignKey("companies.id"), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
