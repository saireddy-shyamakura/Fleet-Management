"""Database session and engine configuration for SQLAlchemy."""

from typing import Generator

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from app.core.config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    echo=False,
    max_overflow=20,
    pool_pre_ping=True,
    pool_size=10,
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)

Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """Yield a database session and close it after use."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_session() -> None:
    """Validate the database session by executing a simple query."""
    db = SessionLocal()
    try:
        result = db.execute(text("SELECT 1"))
        print("Session works:", result.scalar())
    except Exception as error:
        print("Session failed:", error)
    finally:
        db.close()


if __name__ == "__main__":
    test_session()
