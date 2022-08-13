import sqlite3
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# conectar com sqlite
SQLALCHEMY_DATABASE = "backend_test.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///./{SQLALCHEMY_DATABASE}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        print(f'error {e}')
    finally:
        db.close()


