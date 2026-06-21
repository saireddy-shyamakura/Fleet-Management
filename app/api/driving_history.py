from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.driving_history import (
    create_driving_history,
    delete_driving_history,
    get_driving_histories,
    get_driving_history,
    update_driving_history,
)
from app.db import get_db
from app.models import DrivingHistory
from app.schemas.driving_history import (
    DrivingHistoryCreate,
    DrivingHistoryResponse,
    DrivingHistoryUpdate,
)

router = APIRouter(prefix="/driving-history", tags=["driving_history"])


@router.post("/", response_model=DrivingHistoryResponse)
def create(
    data: DrivingHistoryCreate, db: Session = Depends(get_db)
) -> DrivingHistoryResponse:
    return create_driving_history(db, data)


@router.get("/", response_model=list[DrivingHistoryResponse])
def read_all(db: Session = Depends(get_db)) -> list[DrivingHistory]:
    return get_driving_histories(db)


@router.get("/{history_id}", response_model=DrivingHistoryResponse)
def get_history_by_id(
    history_id: int, db: Session = Depends(get_db)
) -> DrivingHistoryResponse:
    history = get_driving_history(db, history_id)
    if history is None:
        raise HTTPException(status_code=404, detail="Driving history not found")
    return history


@router.put("/{history_id}", response_model=DrivingHistoryResponse)
def update_history_by_id(
    history_id: int, data: DrivingHistoryUpdate, db: Session = Depends(get_db)
) -> DrivingHistoryResponse:
    history = update_driving_history(db, history_id, data)
    if history is None:
        raise HTTPException(status_code=404, detail="Driving history not found")
    return history


@router.delete("/{history_id}")
def delete_history_by_id(
    history_id: int, db: Session = Depends(get_db)
) -> dict[str, str]:
    history = delete_driving_history(db, history_id)
    if history is None:
        raise HTTPException(status_code=404, detail="Driving history not found")
    return {"message": "Deleted successfully"}
