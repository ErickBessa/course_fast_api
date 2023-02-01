from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.curso_model import CursoModel
from core.deps import get_session


# Bypass warning sqlmodel select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True # type: ignore
Select.inherit_cache = True # type: ignore
# Fim bypass


router = APIRouter()

# POST Curso
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoModel)
async def post_curso(curso:CursoModel, db: AsyncSession = Depends(get_session)):
    new_course = CursoModel(titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas)
    async with db as session:
        session.add(new_course)
        await session.commit()

    return new_course

"""# POST Cursos
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoModel)
async def post_cursos(cursos:List[CursoModel], db: AsyncSession = Depends(get_session)):
    
    async with db as session:
        for curso in cursos:
            new_course = CursoModel(titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas)
            session.add(new_course)
        
        await session.commit()

    return new_course
"""

# GET Cursos
@router.get('/', status_code=status.HTTP_200_OK,response_model=List[CursoModel])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        courses = result.scalars().all()
        return courses

# GET Curso
@router.get('/{curso_id}', status_code=status.HTTP_200_OK, response_model=CursoModel)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        course: CursoModel = result.scalar_one_or_none()

        if course:
            return course
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Não foi possível encontrar nenhum curso com o id: {curso_id}')


# PUT Curso
@router.put('/{curso_id}', status_code=status.HTTP_200_OK, response_model=CursoModel)
async def put_curso(curso_id: int , curso: CursoModel, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        course: CursoModel = result.scalar_one_or_none()

        if course:
            course.titulo = curso.titulo
            course.horas = curso.horas
            course.aulas = curso.aulas

            await session.commit()
            
            return course
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Não foi possível encontrar nenhum curso com o id: {curso.id}')


# DELETE Curso
@router.delete('/{curso_id}', status_code=status.HTTP_200_OK)
async def del_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        course = result.scalar_one_or_none()

        if course:
            await session.delete(course)
            await session.commit()

            # Colocamos por conta de um bug no FastAPi
            return Response(status_code=status.HTTP_204_NO_CONTENT) 
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Não foi possível encontrar nenhum curso com o id: {curso_id}')