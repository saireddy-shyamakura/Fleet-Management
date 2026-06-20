"""Vehicle model definitions."""

import enum
from datetime import datetime
from typing import Any

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String

from app.db import Base


class VehicleType(enum.Enum):
    """Supported vehicle categories."""

    CAR = "car"
    BIKE = "bike"
    TRUCK = "truck"


class Vehicle(Base):
    """Model for storing vehicle records."""

    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    type: Any = Column(Enum(VehicleType), nullable=False)
    vehicle_number = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    company_id = Column(Integer, ForeignKey("companies.id"))
