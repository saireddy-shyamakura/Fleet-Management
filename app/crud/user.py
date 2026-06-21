from typing import Optional, cast

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import User
from app.schemas.user import UserCreate, UserUpdate


def create_user(db: Session, data: UserCreate) -> User:
    user = User(**data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, user_id: int) -> User | None:
    return cast(Optional[User], db.get(User, user_id))


def get_users(db: Session) -> list[User]:
    return list(db.scalars(select(User)))


def update_user(db: Session, user_id: int, data: UserUpdate) -> User | None:
    user = get_user(db, user_id)
    if not user:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int) -> User | None:
    user = get_user(db, user_id)
    if not user:
        return None

    db.delete(user)
    db.commit()
    return user
