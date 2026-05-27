from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core import config

# This URL pulls from your .env file
DATABASE_URL = config.DATABASE_URL

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set in environment. Check your .env file.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
