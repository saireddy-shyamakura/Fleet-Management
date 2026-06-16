from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR,".env")

load_dotenv(ENV_PATH)

db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_port = os.getenv("DB_PORT")
db_password = os.getenv("DB_PASSWORD")

if not all([db_host, db_name, db_user, db_port, db_password]):
    raise ValueError("Missing database environment variables")

DATABASE_URL = (
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

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