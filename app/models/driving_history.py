"""Driving history model definitions."""

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer

from app.db import Base


class DrivingHistory(Base):
    """Model for storing vehicle trip history."""

    __tablename__ = "driving_history"

    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    driver_id = Column(Integer, ForeignKey("users.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime, nullable=True)
    start_lat = Column(Float)
    start_lon = Column(Float)
    end_lat = Column(Float)
    end_lon = Column(Float)
    distance = Column(Float)
