from typing import Optional, cast

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Vehicle
from app.schemas.vehicle import VehicleCreate, VehicleUpdate


def create_vehicle(db: Session, data: VehicleCreate) -> Vehicle:
    vehicle = Vehicle(**data.model_dump())
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle


def get_vehicle(db: Session, vehicle_id: int) -> Vehicle | None:
    return cast(Optional[Vehicle], db.get(Vehicle, vehicle_id))


def get_vehicles(db: Session) -> list[Vehicle]:
    return list(db.scalars(select(Vehicle)))


def update_vehicle(db: Session, vehicle_id: int, data: VehicleUpdate) -> Vehicle | None:
    vehicle = get_vehicle(db, vehicle_id)
    if not vehicle:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(vehicle, key, value)

    db.commit()
    db.refresh(vehicle)
    return vehicle


def delete_vehicle(db: Session, vehicle_id: int) -> Vehicle | None:
    vehicle = get_vehicle(db, vehicle_id)
    if not vehicle:
        return None

    db.delete(vehicle)
    db.commit()
    return vehicle
