from typing import Optional, cast

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Telemetry
from app.schemas.telemetry import TelemetryCreate, TelemetryUpdate


def create_telemetry(db: Session, data: TelemetryCreate) -> Telemetry:
    telemetry = Telemetry(**data.model_dump())
    db.add(telemetry)
    db.commit()
    db.refresh(telemetry)
    return telemetry


def get_telemetry(db: Session, telemetry_id: int) -> Telemetry | None:
    return cast(Optional[Telemetry], db.get(Telemetry, telemetry_id))


def get_telemetries(db: Session) -> list[Telemetry]:
    return list(db.scalars(select(Telemetry)))


def update_telemetry(
    db: Session, telemetry_id: int, data: TelemetryUpdate
) -> Telemetry | None:
    telemetry = get_telemetry(db, telemetry_id)
    if not telemetry:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(telemetry, key, value)

    db.commit()
    db.refresh(telemetry)
    return telemetry


def delete_telemetry(db: Session, telemetry_id: int) -> Telemetry | None:
    telemetry = get_telemetry(db, telemetry_id)
    if not telemetry:
        return None

    db.delete(telemetry)
    db.commit()
    return telemetry
