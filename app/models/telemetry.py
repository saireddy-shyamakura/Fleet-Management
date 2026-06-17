from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from datetime import datetime
from app.db import Base

class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))

    timestamp = Column(DateTime, default=datetime.utcnow)

    speed = Column(Float)
    engine_temp = Column(Float)
    battery = Column(Float)

    latitude = Column(Float)
    longitude = Column(Float)