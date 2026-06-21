from typing import Optional, cast

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import VehicleSettings
from app.schemas.vehicle_settings import VehicleSettingsCreate, VehicleSettingsUpdate


def create_vehicle_settings(
    db: Session, data: VehicleSettingsCreate
) -> VehicleSettings:
    settings = VehicleSettings(**data.model_dump())
    db.add(settings)
    db.commit()
    db.refresh(settings)
    return settings


def get_vehicle_settings(db: Session, settings_id: int) -> VehicleSettings | None:
    return cast(Optional[VehicleSettings], db.get(VehicleSettings, settings_id))


def get_vehicle_settings_list(db: Session) -> list[VehicleSettings]:
    return list(db.scalars(select(VehicleSettings)))


def update_vehicle_settings(
    db: Session, settings_id: int, data: VehicleSettingsUpdate
) -> VehicleSettings | None:
    settings = get_vehicle_settings(db, settings_id)
    if not settings:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(settings, key, value)

    db.commit()
    db.refresh(settings)
    return settings


def delete_vehicle_settings(db: Session, settings_id: int) -> VehicleSettings | None:
    settings = get_vehicle_settings(db, settings_id)
    if not settings:
        return None

    db.delete(settings)
    db.commit()
    return settings
