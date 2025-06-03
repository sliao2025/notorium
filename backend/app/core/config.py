# app/core/config.py
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",
        "http://localhost:3001",
    ]
    UPLOAD_DIR: str = "/tmp/uploads"
    MIDI_DIR: str = "/tmp/midi"

    class Config:
        env_file = ".env"

settings = Settings()