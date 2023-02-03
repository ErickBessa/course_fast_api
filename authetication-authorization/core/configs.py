from typing import List
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://dev:dev@localhost:5432/dev'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = 'wluCnq6r-qN0_LG0eqVZjRtj_-QyD_72snaYsWG4Exw'
    """
    # Como gerar um token usando o python
    import secrets
    token:str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'
    
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings: Settings = Settings()