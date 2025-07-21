from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from core.config import settings


DATABASE_URL = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@localhost:{settings.DB_PORT}/{settings.DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
