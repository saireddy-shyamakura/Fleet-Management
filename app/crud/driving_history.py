from typing import Optional, cast

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import DrivingHistory
from app.schemas.driving_history import DrivingHistoryCreate, DrivingHistoryUpdate


def create_driving_history(db: Session, data: DrivingHistoryCreate) -> DrivingHistory:
    history = DrivingHistory(**data.model_dump())
    db.add(history)
    db.commit()
    db.refresh(history)
    return history


def get_driving_history(db: Session, history_id: int) -> DrivingHistory | None:
    return cast(Optional[DrivingHistory], db.get(DrivingHistory, history_id))


def get_driving_histories(db: Session) -> list[DrivingHistory]:
    return list(db.scalars(select(DrivingHistory)))


def update_driving_history(
    db: Session, history_id: int, data: DrivingHistoryUpdate
) -> DrivingHistory | None:
    history = get_driving_history(db, history_id)
    if not history:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(history, key, value)

    db.commit()
    db.refresh(history)
    return history


def delete_driving_history(db: Session, history_id: int) -> DrivingHistory | None:
    history = get_driving_history(db, history_id)
    if not history:
        return None

    db.delete(history)
    db.commit()
    return history
