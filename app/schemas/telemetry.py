from datetime import datetime

from pydantic import BaseModel


class TelemetryBase(BaseModel):
    vehicle_id: int
    company_id: int
    timestamp: datetime | None = None
    speed: float
    engine_temp: float
    battery: float
    latitude: float
    longitude: float


class TelemetryCreate(TelemetryBase):
    pass


class TelemetryUpdate(BaseModel):
    vehicle_id: int | None = None
    company_id: int | None = None
    timestamp: datetime | None = None
    speed: float | None = None
    engine_temp: float | None = None
    battery: float | None = None
    latitude: float | None = None
    longitude: float | None = None


class TelemetryResponse(TelemetryBase):
    id: int

    class Config:
        from_attributes = True
