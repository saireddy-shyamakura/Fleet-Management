from datetime import datetime

from pydantic import BaseModel


class DrivingHistoryBase(BaseModel):
    vehicle_id: int
    driver_id: int
    company_id: int
    start_time: datetime
    end_time: datetime | None = None
    start_lat: float
    start_lon: float
    end_lat: float
    end_lon: float
    distance: float


class DrivingHistoryCreate(DrivingHistoryBase):
    pass


class DrivingHistoryUpdate(BaseModel):
    vehicle_id: int | None = None
    driver_id: int | None = None
    company_id: int | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None
    start_lat: float | None = None
    start_lon: float | None = None
    end_lat: float | None = None
    end_lon: float | None = None
    distance: float | None = None


class DrivingHistoryResponse(DrivingHistoryBase):
    id: int

    class Config:
        from_attributes = True
