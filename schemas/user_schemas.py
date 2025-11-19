from datetime import datetime, date
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    nombre: str = Field(..., max_length=150)
    apellidos: str = Field(..., max_length=150)
    email: EmailStr = Field(..., max_length=150)
    key: str = Field(..., max_length=100, min_length=8)
    fecha_nacimiento: date
