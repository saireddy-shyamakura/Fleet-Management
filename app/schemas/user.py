from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr


class UserRole(str, Enum):
    ADMIN = "admin"
    DRIVER = "driver"
    SUPERADMIN = "superadmin"


class UserBase(BaseModel):
    email: EmailStr
    role: UserRole
    company_id: int | None = None


class UserCreate(UserBase):
    hashed_password: str


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    role: UserRole | None = None
    hashed_password: str | None = None
    company_id: int | None = None


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
