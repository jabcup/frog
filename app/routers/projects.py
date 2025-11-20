from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, and_, true
from sqlalchemy.exc import SQLAlchemyError
from app.schemas.project_schemas import ProjectCreate, ProjectList
from app.db.session import SessionLocal
from app.db.models import Proyecto, Usuario
from app.auth import get_current_user

router = APIRouter(tags=["projects"])


@router.post("/new_project")
def create_project(project: ProjectCreate, user_id=Depends(get_current_user)):
    try:
        with SessionLocal() as session:
            usuario = session.get(Usuario, int(user_id["id"]))
            new_project = Proyecto(
                usuario=usuario, nombre=project.nombre, descripcion=project.descripcion
            )
            session.add(new_project)
            session.commit()

        return True
    except SQLAlchemyError:
        return "auxilio auxilio, error de sqlalchemy"


@router.get("/projects")
def get_project_list(user_id=Depends(get_current_user)):
    try:
        with SessionLocal() as session:
            usuario = session.get(Usuario, int(user_id["id"]))
            project_list = select(Proyecto).where(Proyecto.usuario == usuario)
            project_list = session.scalars(project_list).all()

        return project_list

    except SQLAlchemyError:
        return "error con sqlalchemy"
