from fastapi import FastAPI
from db.base_class import Base
from db.sessions import engine
from user.models import User

app = FastAPI(title="Routine Maaster")

Base.metadata.create_all(bind=engine) # type: ignore

@app.get("/health-cheack")
def health_check():
    return "All good"