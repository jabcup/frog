from fastapi import APIRouter, Path, HTTPException
from sqlalchemy import select, and_
from sqlalchemy.exc import SQLAlchemyError
from app.db.models import *
from app.schemas.general_schemas import *
from app.db.session import SessionLocal

router = APIRouter(tags=["showdata"])


@router.get("/dato/{id}")
def show_dato(id=Path(..., description="id del dato en cuestion")):
    try:
        with SessionLocal() as session:
            dato_en_cuestion = session.get(Dato, id)

        return {"dato": dato_en_cuestion}

    except:
        return f"error obteniendo el dato con id: {id}"


@router.get("/recurso/{id}")
def show_recurso(id=Path(..., description="id del dato en cuestion")):
    try:
        with SessionLocal() as session:
            recurso_en_cuestion = session.get(Recurso, id)

        return {"recurso": recurso_en_cuestion}

    except:
        return f"error obteniendo el recurso con id: {id}"


@router.get("/etiqueta/{id}")
def show_tag(id=Path(..., description="id del dato en cuestion")):
    try:
        with SessionLocal() as session:
            tag_en_cuestion = session.get(Etiqueta, id)

        return {"etiqueta": tag_en_cuestion}

    except:
        return f"error obteniendo la etiqueta con id: {id}"


@router.get("/enlace/{id}")
def show_enlace(id=Path(..., description="id del dato en cuestion")):
    try:
        with SessionLocal() as session:
            enlace_en_cuestion = session.get(Enlace, id)

        return {"dato": enlace_en_cuestion}

    except:
        return f"error obteniendo el enlace con id: {id}"


@router.get("/tarea/{id}")
def show_tarea(id=Path(..., description="id del dato en cuestion")):
    try:
        with SessionLocal() as session:
            tarea_en_cuestion = session.get(Tarea, id)

        return {"tarea": tarea_en_cuestion}

    except:
        return f"error obteniendo la tarea con id: {id}"


@router.get("/evento/{id}")
def show_evento(id=Path(..., description="id del dato en cuestion")):
    try:
        with SessionLocal() as session:
            evento_en_cuestion = session.get(Evento, id)

        return {"evento": evento_en_cuestion}

    except:
        return f"error obteniendo el evento con id: {id}"
