from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    pool_size = 10,
    max_overflow = 20,
    echo = False,
    pool_pre_ping=True
    )

SessionLocal = sessionmaker(
    bind=engine,
    autoflush = False,
    autocommit = False
    )

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_session():
    db = SessionLocal()
    try:
        result = db.execute(text("SELECT 1"))
        print("Session works:", result.scalar())
    except Exception as e:
       print("session failed",e)
    finally:
        db.close()


if __name__ == "__main__":
    test_session()