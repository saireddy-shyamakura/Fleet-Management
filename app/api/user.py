from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.user import (
    create_user,
    delete_user,
    get_user,
    get_users,
    update_user,
)
from app.db import get_db
from app.models import User
from app.schemas.user import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse)
def create(data: UserCreate, db: Session = Depends(get_db)) -> UserResponse:
    return create_user(db, data)


@router.get("/", response_model=list[UserResponse])
def read_all(db: Session = Depends(get_db)) -> list[User]:
    return get_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)) -> UserResponse:
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserResponse)
def update_user_by_id(
    user_id: int, data: UserUpdate, db: Session = Depends(get_db)
) -> UserResponse:
    user = update_user(db, user_id, data)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}")
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    user = delete_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Deleted successfully"}
