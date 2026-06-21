from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.telemetry import (
    create_telemetry,
    delete_telemetry,
    get_telemetries,
    get_telemetry,
    update_telemetry,
)
from app.db import get_db
from app.models import Telemetry
from app.schemas.telemetry import TelemetryCreate, TelemetryResponse, TelemetryUpdate

router = APIRouter(prefix="/telemetry", tags=["telemetry"])


@router.post("/", response_model=TelemetryResponse)
def create(data: TelemetryCreate, db: Session = Depends(get_db)) -> TelemetryResponse:
    return create_telemetry(db, data)


@router.get("/", response_model=list[TelemetryResponse])
def read_all(db: Session = Depends(get_db)) -> list[Telemetry]:
    return get_telemetries(db)


@router.get("/{telemetry_id}", response_model=TelemetryResponse)
def get_telemetry_by_id(
    telemetry_id: int, db: Session = Depends(get_db)
) -> TelemetryResponse:
    telemetry = get_telemetry(db, telemetry_id)
    if telemetry is None:
        raise HTTPException(status_code=404, detail="Telemetry record not found")
    return telemetry


@router.put("/{telemetry_id}", response_model=TelemetryResponse)
def update_telemetry_by_id(
    telemetry_id: int, data: TelemetryUpdate, db: Session = Depends(get_db)
) -> TelemetryResponse:
    telemetry = update_telemetry(db, telemetry_id, data)
    if telemetry is None:
        raise HTTPException(status_code=404, detail="Telemetry record not found")
    return telemetry


@router.delete("/{telemetry_id}")
def delete_telemetry_by_id(
    telemetry_id: int, db: Session = Depends(get_db)
) -> dict[str, str]:
    telemetry = delete_telemetry(db, telemetry_id)
    if telemetry is None:
        raise HTTPException(status_code=404, detail="Telemetry record not found")
    return {"message": "Deleted successfully"}
