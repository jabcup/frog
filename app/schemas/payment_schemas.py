from datetime import datetime
from pydantic import BaseModel, Field, EmailStr

# quiero que el endpoint reciba el usuario, el usuario tiene que tener el rol de deudor (el 3) y existir, si existe se valida la información del pago (aun no se como), y si todo funca como tiene que funcar se le cambia el rol de 3 a 1 (de deudor a usuario)
#


class PaymentGet(BaseModel):
    cliente: str = Field(max_length=255)
    correo: EmailStr = Field(max_length=150)
    cvv: int = Field(...)
    fecha_exp: str
    cc: str = Field(..., min_length=13, max_length=19)
    concepto: str = Field(..., max_length=255)
    monto: float
    nit: int = Field(...)
