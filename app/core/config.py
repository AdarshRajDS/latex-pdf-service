import os
from pydantic_settings import BaseSettings

TIMEOUT = int(os.getenv("TIMEOUT", 60))

class Settings(BaseSettings):
    APP_NAME: str = "latex-pdf-service"
    TIMEOUT: int = TIMEOUT
    TMP_DIR: str = "/tmp/latex"

settings = Settings()
