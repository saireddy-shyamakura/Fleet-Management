from typing import Optional, cast

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Alert
from app.schemas.alert import AlertCreate, AlertUpdate


def create_alert(db: Session, data: AlertCreate) -> Alert:
    alert = Alert(**data.model_dump())
    db.add(alert)
    db.commit()
    db.refresh(alert)
    return alert


def get_alert(db: Session, alert_id: int) -> Alert | None:
    return cast(Optional[Alert], db.get(Alert, alert_id))


def get_alerts(db: Session) -> list[Alert]:
    return list(db.scalars(select(Alert)))


def update_alert(db: Session, alert_id: int, data: AlertUpdate) -> Alert | None:
    alert = get_alert(db, alert_id)
    if not alert:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(alert, key, value)

    db.commit()
    db.refresh(alert)
    return alert


def delete_alert(db: Session, alert_id: int) -> Alert | None:
    alert = get_alert(db, alert_id)
    if not alert:
        return None

    db.delete(alert)
    db.commit()
    return alert
