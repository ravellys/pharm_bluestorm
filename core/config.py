import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_TITLE: str = "Pharm Bluestorm"
    PROJECT_VERSION: str = "0.0.1"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"


settings = Settings()
