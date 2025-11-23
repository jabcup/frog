from fastapi import APIRouter, HTTPException
from sqlalchemy import select, and_
from sqlalchemy.exc import SQLAlchemyError
from app.db.models import Dato, Enlace, Proyecto, Evento, Recurso, Tarea, TipoRecurso
from app.schemas.general_schemas import (
    DatoCreate,
    EnlaceCreate,
    RecursoCreate,
    TareaCreate,
    EventoCreate,
)
from app.db.session import SessionLocal


router = APIRouter(tags=["data"])


@router.post("/new_data")
def new_data(nuevo_dato: DatoCreate):
    try:
        with SessionLocal() as get_project:
            project = get_project.get(Proyecto, nuevo_dato.id_proyecto)

        data_to_add = Dato(
            proyecto=project,
            titulo=nuevo_dato.titulo,
            contenido=nuevo_dato.contenido,
            importancia=nuevo_dato.importancia,
            etiquetas=nuevo_dato.etiquetas,
        )

        try:
            with SessionLocal() as session:
                session.add(data_to_add)
                session.commit()

            return {"resultao": "correcto papacho, nuevo dato dateado en la data"}
        except:  # tambien se que no hay que ponerle except crudo pero por ahora sirve
            print("error creando los datos")
    except:
        print(
            "error encontrando el proyecto"
        )  # se que no hay que hacerlo con print pero luego lo arreglo


@router.post("/new_event")
def new_event(nuevo_evento: EventoCreate):
    try:
        with SessionLocal() as get_project:
            project = get_project.get(Proyecto, nuevo_evento.id_proyecto)

        data_to_add = Evento(
            proyecto=project,
            nombre=nuevo_evento.nombre,
            descripcion=nuevo_evento.descripcion,
            fecha_hora_evento=nuevo_evento.fecha_evento,
            recordatorio=nuevo_evento.recordatorio,
            tipo=nuevo_evento.tipo,
        )

        try:
            with SessionLocal() as session:
                session.add(data_to_add)
                session.commit()

            return {"resultao": "correcto papacho, nuevo dato dateado en la data"}
        except:  # tambien se que no hay que ponerle except crudo pero por ahora sirve
            print("error creando los datos")
    except:
        print(
            "error encontrando el proyecto"
        )  # se que no hay que hacerlo con print pero luego lo arreglo


@router.post("/new_task")
def new_task(nueva_tarea: TareaCreate):
    try:
        with SessionLocal() as get_project:
            project = get_project.get(Proyecto, nueva_tarea.id_proyecto)

        data_to_add = Tarea(
            proyecto=project,
            nombre=nueva_tarea.nombre,
            descripcion=nueva_tarea.descripcion,
            fecha_hora_evento=nueva_tarea.fecha_evento,
            recordatorio=nueva_tarea.recordatorio,
            importancia=nueva_tarea.importancia,
            estado=nueva_tarea.estado,
        )

        try:
            with SessionLocal() as session:
                session.add(data_to_add)
                session.commit()

            return {"resultao": "correcto papacho, nuevo dato dateado en la data"}
        except:  # tambien se que no hay que ponerle except crudo pero por ahora sirve
            print("error creando los datos")
    except:
        print(
            "error encontrando el proyecto"
        )  # se que no hay que hacerlo con print pero luego lo arreglo


@router.post("/new_resource")
def new_res(nuevo_recurso: RecursoCreate):
    try:
        with SessionLocal() as get_project:
            project = get_project.get(Proyecto, nuevo_recurso.id_proyecto)
            tipo_r = get_project.get(TipoRecurso, nuevo_recurso.id_tipo)

        data_to_add = Recurso(
            proyecto=project,
            tipo=tipo_r,
            relevancia=nuevo_recurso.relevancia,
            url=nuevo_recurso.url,
        )

        try:
            with SessionLocal() as session:
                session.add(data_to_add)
                session.commit()

            return {"resultao": "correcto papacho, nuevo dato dateado en la data"}
        except:  # tambien se que no hay que ponerle except crudo pero por ahora sirve
            print("error creando los datos")
    except SQLAlchemyError as e:
        print(
            "error encontrando el proyecto ", e
        )  # se que no hay que hacerlo con print pero luego lo arreglo


@router.post("/new_link")
def new_link(nuevo_enlace: EnlaceCreate):
    try:
        with SessionLocal() as get_project:
            project = get_project.get(Proyecto, nuevo_enlace.id_proyecto)

        data_to_add = Enlace(
            proyecto=project,
            origen=nuevo_enlace.origen,
            destino=nuevo_enlace.destino,
            tipo_origen=nuevo_enlace.tipo_origen,
            tipo_destino=nuevo_enlace.tipo_destino,
        )

        try:
            with SessionLocal() as session:
                session.add(data_to_add)
                session.commit()

            return {"resultao": "correcto papacho, nuevo dato dateado en la data"}
        except:  # tambien se que no hay que ponerle except crudo pero por ahora sirve
            print("error creando los datos")
    except SQLAlchemyError as e:
        print(
            "error encontrando el proyecto ", e
        )  # se que no hay que hacerlo con print pero luego lo arreglo
