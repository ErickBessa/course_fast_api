from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL



class Settings(BaseSettings):
    '''
    Configurações gerais usadas na aplicação.
    '''
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://dev:dev@localhost:5432/dev'
    DBBaseModel = declarative_base()

    class Config:
        case_sentitive = True


settings = Settings()