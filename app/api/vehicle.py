from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.vehicle import (
    create_vehicle,
    delete_vehicle,
    get_vehicle,
    get_vehicles,
    update_vehicle,
)
from app.db import get_db
from app.models import Vehicle
from app.schemas.vehicle import VehicleCreate, VehicleResponse, VehicleUpdate

router = APIRouter(prefix="/vehicles", tags=["vehicles"])


@router.post("/", response_model=VehicleResponse)
def create(data: VehicleCreate, db: Session = Depends(get_db)) -> VehicleResponse:
    return create_vehicle(db, data)


@router.get("/", response_model=list[VehicleResponse])
def read_all(db: Session = Depends(get_db)) -> list[Vehicle]:
    return get_vehicles(db)


@router.get("/{vehicle_id}", response_model=VehicleResponse)
def get_vehicle_by_id(
    vehicle_id: int, db: Session = Depends(get_db)
) -> VehicleResponse:
    vehicle = get_vehicle(db, vehicle_id)
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle


@router.put("/{vehicle_id}", response_model=VehicleResponse)
def update_vehicle_by_id(
    vehicle_id: int, data: VehicleUpdate, db: Session = Depends(get_db)
) -> VehicleResponse:
    vehicle = update_vehicle(db, vehicle_id, data)
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle


@router.delete("/{vehicle_id}")
def delete_vehicle_by_id(
    vehicle_id: int, db: Session = Depends(get_db)
) -> dict[str, str]:
    vehicle = delete_vehicle(db, vehicle_id)
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return {"message": "Deleted successfully"}
