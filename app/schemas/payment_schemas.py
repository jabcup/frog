from datetime import datetime
from pydantic import BaseModel, Field, EmailStr

# quiero que el endpoint reciba el usuario, el usuario tiene que tener el rol de deudor (el 3) y existir, si existe se valida la información del pago (aun no se como), y si todo funca como tiene que funcar se le cambia el rol de 3 a 1 (de deudor a usuario)
#


class PaymentGet(BaseModel):
    nombres: str
    apellidos: str
    cvv: int = Field(...)
    fecha_exp: str
    cc: str = Field(..., min_length=13, max_length=19)
