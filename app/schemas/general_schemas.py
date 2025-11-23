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
    estado: bool = Field(default=False)


class RecursoCreate(BaseModel):
    id_proyecto: int = Field(...)
    id_tipo: int = Field(default=2)
    relevancia: int
    url: str = Field(default="ninguna", max_length=255)


class EnlaceCreate(BaseModel):
    id_proyecto: int = Field(...)
    origen: int = Field(...)
    destino: int = Field(...)
    tipo_origen: str = Field(..., max_length=50)
    tipo_destino: str = Field(..., max_length=50)


class CodigoCreate(BaseModel):
    factura_id: int = Field(...)
    banco: str = Field(max_length=20)
    impuesto: str = Field(max_length=20)
    contab: str = Field(max_length=20)


class EtiquetaCreate(BaseModel):
    id_proyecto: int = Field(...)
    nombre: str = Field(..., max_length=50)
    descripcion: str = Field(max_length=150)
    color: str = Field(default="#404040")
