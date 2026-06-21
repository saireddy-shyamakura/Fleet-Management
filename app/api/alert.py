from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.alert import (
    create_alert,
    delete_alert,
    get_alert,
    get_alerts,
    update_alert,
)
from app.db import get_db
from app.models import Alert
from app.schemas.alert import AlertCreate, AlertResponse, AlertUpdate

router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.post("/", response_model=AlertResponse)
def create(data: AlertCreate, db: Session = Depends(get_db)) -> AlertResponse:
    return create_alert(db, data)


@router.get("/", response_model=list[AlertResponse])
def read_all(db: Session = Depends(get_db)) -> list[Alert]:
    return get_alerts(db)


@router.get("/{alert_id}", response_model=AlertResponse)
def get_alert_by_id(alert_id: int, db: Session = Depends(get_db)) -> AlertResponse:
    alert = get_alert(db, alert_id)
    if alert is None:
        raise HTTPException(status_code=404, detail="Alert not found")
    return alert


@router.put("/{alert_id}", response_model=AlertResponse)
def update_alert_by_id(
    alert_id: int, data: AlertUpdate, db: Session = Depends(get_db)
) -> AlertResponse:
    alert = update_alert(db, alert_id, data)
    if alert is None:
        raise HTTPException(status_code=404, detail="Alert not found")
    return alert


@router.delete("/{alert_id}")
def delete_alert_by_id(alert_id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    alert = delete_alert(db, alert_id)
    if alert is None:
        raise HTTPException(status_code=404, detail="Alert not found")
    return {"message": "Deleted successfully"}
