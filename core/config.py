from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BASE_URL: str = "http://localhost:8000"
    PROJECT_NAME: str = "RoutineMaaster"
    DB_USER:str
    DB_PASSWORD:str
    DB_NAME:str
    DB_PORT:str    




    class Config:
        env_file = ".env"

settings = Settings() # type: ignore