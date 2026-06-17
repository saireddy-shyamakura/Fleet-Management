from sqlalchemy import Column , Integer, String , DateTime, ForeignKey, Boolean, Enum
from app.db import Base
from datetime import datetime
import enum

class VehicleType(enum.Enum):
    CAR = "car"
    BIKE = "bike"
    TRUCK = "truck"


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    type = Column(Enum(VehicleType), nullable=False)
    vehicle_number = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    company_id = Column(Integer, ForeignKey("companies.id"))
