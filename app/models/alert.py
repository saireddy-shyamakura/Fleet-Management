from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from datetime import datetime
from app.db import Base
import enum

class AlertType(enum.Enum):
    OVERSPEED = "overspeed"
    GEOFENCE = "geofence"
    OVERHEATING = "overheating"


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))

    alert_type = Column(Enum(AlertType))
    message = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)