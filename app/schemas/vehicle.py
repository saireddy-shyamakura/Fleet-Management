from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class VehicleType(str, Enum):
    CAR = "car"
    BIKE = "bike"
    TRUCK = "truck"


class VehicleBase(BaseModel):
    type: VehicleType
    vehicle_number: str
    company_id: int


class VehicleCreate(VehicleBase):
    is_active: bool | None = True


class VehicleUpdate(BaseModel):
    type: VehicleType | None = None
    vehicle_number: str | None = None
    company_id: int | None = None
    is_active: bool | None = None


class VehicleResponse(VehicleBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
