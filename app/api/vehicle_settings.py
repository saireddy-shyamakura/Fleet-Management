from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.vehicle_settings import (
    create_vehicle_settings,
    delete_vehicle_settings,
    get_vehicle_settings,
    get_vehicle_settings_list,
    update_vehicle_settings,
)
from app.db import get_db
from app.models import VehicleSettings
from app.schemas.vehicle_settings import (
    VehicleSettingsCreate,
    VehicleSettingsResponse,
    VehicleSettingsUpdate,
)

router = APIRouter(prefix="/vehicle-settings", tags=["vehicle_settings"])


@router.post("/", response_model=VehicleSettingsResponse)
def create(
    data: VehicleSettingsCreate, db: Session = Depends(get_db)
) -> VehicleSettingsResponse:
    return create_vehicle_settings(db, data)


@router.get("/", response_model=list[VehicleSettingsResponse])
def read_all(db: Session = Depends(get_db)) -> list[VehicleSettings]:
    return get_vehicle_settings_list(db)


@router.get("/{settings_id}", response_model=VehicleSettingsResponse)
def get_settings_by_id(
    settings_id: int, db: Session = Depends(get_db)
) -> VehicleSettingsResponse:
    settings = get_vehicle_settings(db, settings_id)
    if settings is None:
        raise HTTPException(status_code=404, detail="Vehicle settings not found")
    return settings


@router.put("/{settings_id}", response_model=VehicleSettingsResponse)
def update_settings_by_id(
    settings_id: int, data: VehicleSettingsUpdate, db: Session = Depends(get_db)
) -> VehicleSettingsResponse:
    settings = update_vehicle_settings(db, settings_id, data)
    if settings is None:
        raise HTTPException(status_code=404, detail="Vehicle settings not found")
    return settings


@router.delete("/{settings_id}")
def delete_settings_by_id(
    settings_id: int, db: Session = Depends(get_db)
) -> dict[str, str]:
    settings = delete_vehicle_settings(db, settings_id)
    if settings is None:
        raise HTTPException(status_code=404, detail="Vehicle settings not found")
    return {"message": "Deleted successfully"}
