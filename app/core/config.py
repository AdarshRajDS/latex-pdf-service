from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "latex-pdf-service"
    TIMEOUT: int = 15
    TMP_DIR: str = "/tmp/latex"

settings = Settings()
