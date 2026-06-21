from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class AlertType(str, Enum):
    GEOFENCE = "geofence"
    OVERHEATING = "overheating"
    OVERSPEED = "overspeed"


class AlertBase(BaseModel):
    vehicle_id: int
    company_id: int
    alert_type: AlertType
    message: str


class AlertCreate(AlertBase):
    pass


class AlertUpdate(BaseModel):
    vehicle_id: int | None = None
    company_id: int | None = None
    alert_type: AlertType | None = None
    message: str | None = None


class AlertResponse(AlertBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
