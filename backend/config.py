import os
from pydantic import BaseSettings

class Config(BaseSettings):
    DATABASE_URL: str = "sqlite:///./database.db"
    PDF_STORAGE_PATH: str = "./uploads"
    MAX_UPLOAD_SIZE_MB: int = 10
    RATE_LIMIT: str = "10/minute"  # Example rate limit

    class Config:
        env_file = ".env"
