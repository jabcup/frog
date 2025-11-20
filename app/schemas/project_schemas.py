from datetime import date, datetime
from pydantic import BaseModel, Field


class ProjectCreate(BaseModel):
    nombre: str = Field(default="Proyecto", max_length=100)
    descripcion: str


class ProjectList(BaseModel):
    nombre: str
    descripcion: str
    fecha_creacion: date
    estado: bool
