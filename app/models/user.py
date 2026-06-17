from sqlalchemy import Column, String , Integer, DateTime, ForeignKey, Enum
from datetime import datetime
from app.db import Base

import enum

class UserRole(enum.Enum):
    DRIVER = "driver"
    ADMIN = "admin"
    SUPERADMIN = "superadmin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)

    company_id = Column(Integer, ForeignKey("companies.id"), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)