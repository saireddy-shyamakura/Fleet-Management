from sqlalchemy import Column, Integer, Float, ForeignKey
from app.db import Base

class VehicleSettings(Base):
    __tablename__ = "vehicle_settings"

    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), unique=True)

    overspeed_limit = Column(Float)
    geofence_lat = Column(Float)
    geofence_lon = Column(Float)
    geofence_radius = Column(Float)
    max_temp = Column(Float)