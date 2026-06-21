from pydantic import BaseModel


class VehicleSettingsBase(BaseModel):
    vehicle_id: int
    overspeed_limit: float
    geofence_lat: float
    geofence_lon: float
    geofence_radius: float
    max_temp: float


class VehicleSettingsCreate(VehicleSettingsBase):
    pass


class VehicleSettingsUpdate(BaseModel):
    vehicle_id: int | None = None
    overspeed_limit: float | None = None
    geofence_lat: float | None = None
    geofence_lon: float | None = None
    geofence_radius: float | None = None
    max_temp: float | None = None


class VehicleSettingsResponse(VehicleSettingsBase):
    id: int

    class Config:
        from_attributes = True
