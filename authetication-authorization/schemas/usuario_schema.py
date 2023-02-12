from typing import Optional
from typing import List

from pydantic import BaseModel, EmailStr
from sqlalchemy.sql.sqltypes import Boolean

from schemas.artigo_schema import ArtigoSchema


class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False


    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str 


class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]


class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin: Optional[Boolean]