from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Literal


class DatoCreate(BaseModel):
    titulo: str = Field(default="Dato", max_length=150)
    contenido: str = Field(..., max_length=255)
    importancia: int = Field(default=0)
    etiquetas: list[int] = Field(default_factory=list)
    id_proyecto: int = Field(...)


class EventoCreate(BaseModel):
    id_proyecto: int
    nombre: str = Field(..., max_length=100)
    descripcion: str = Field(default="", max_length=255)
    fecha_evento: datetime
    recordatorio: bool = False
    tipo: Literal["evento"] = "evento"


class TareaCreate(EventoCreate):
    tipo: Literal["tarea"] = "tarea"
    importancia: int
    estado: bool = False
