from fastapi import APIRouter, HTTPException, Path
from sqlalchemy import select, and_
from sqlalchemy.exc import SQLAlchemyError
from app.db.models import *
from app.schemas.general_schemas import *
from app.db.session import SessionLocal

router = APIRouter(tags=["listdata"])


@router.get("/list_data/{id_proyecto}")
def list_data(id_proyecto=Path(..., description="id del proyecto")):
    try:
        with SessionLocal() as session:
            project = session.get(Proyecto, id_proyecto)
            datos = select(Dato).where(Dato.proyecto == project)
            lista_datos = session.scalars(datos).all()

        return {"datos": lista_datos}
    except:
        return "error obteniendo la lista de datos"


@router.get("/list_tasks/{id_proyecto}")
def list_tasks(id_proyecto=Path(..., description="id del proyecto")):
    try:
        with SessionLocal() as session:
            project = session.get(Proyecto, id_proyecto)
            tareas = select(Tarea).where(Tarea.proyecto == project)
            lista = session.scalars(tareas).all()

        return {"tareas": lista}
    except:
        return "error obteniendo la lista"


@router.get("/list_events/{id_proyecto}")
def list_events(id_proyecto=Path(..., description="id del proyecto")):
    try:
        with SessionLocal() as session:
            project = session.get(Proyecto, id_proyecto)
            eventos = select(Evento).where(Evento.proyecto == project)
            lista = session.scalars(eventos).all()

        return {"eventos": lista}
    except:
        return "error obteniendo la lista"


@router.get("/list_resources/{id_proyecto}")
def list_res(id_proyecto=Path(..., description="id del proyecto")):
    try:
        with SessionLocal() as session:
            project = session.get(Proyecto, id_proyecto)
            recursos = select(Recurso).where(Recurso.proyecto == project)
            lista = session.scalars(recursos).all()

        return {"recursos": lista}
    except:
        return "error obteniendo la lista"


@router.get("/list_tags/{id_proyecto}")
def list_tags(id_proyecto=Path(..., description="id del proyecto")):
    try:
        with SessionLocal() as session:
            project = session.get(Proyecto, id_proyecto)
            etiquetas = select(Etiqueta).where(Etiqueta.proyecto == project)
            lista = session.scalars(etiquetas).all()

        return {"etiquetas": lista}
    except:
        return "error obteniendo la lista"


@router.get("/list_links/{id_proyecto}")
def list_links(id_proyecto=Path(..., description="id del proyecto")):
    try:
        with SessionLocal() as session:
            project = session.get(Proyecto, id_proyecto)
            enlaces = select(Enlace).where(Enlace.proyecto == project)
            lista = session.scalars(enlaces).all()

        return {"enlaces": lista}
    except:
        return "error obteniendo la lista"
