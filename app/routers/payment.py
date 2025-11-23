from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import exists, select, and_
from sqlalchemy.exc import SQLAlchemyError
from app.schemas.payment_schemas import PaymentGet

# debo tener un modelo pydantic que valide el usuario? creo que sí no? o lo manejo con la session
from app.db.session import SessionLocal
from app.db.models import Factura, Usuario

# from app.schemas.user_schemas import
from app.auth import (
    get_current_user,
)  # creo que obtengo el usuario, si el usuario es válido entonces tenemos listo el id no?

router = APIRouter(tags=["payments"])


@router.post("/generate_payment")
def generate_payment(
    payment_data: PaymentGet, user_id: str = Depends(get_current_user)
):
    with SessionLocal() as session:
        user = session.get(Usuario, int(user_id["id"]))

    if user.rol_id == 3 and user.estado:
        with SessionLocal() as session:
            user.rol_id = 1
            session.add(user)
            factura = Factura(
                usuario=user,
                nit=payment_data.nit,
                concepto=payment_data.concepto,
                monto=payment_data.monto,
                correo_destino=payment_data.correo,
                cliente=payment_data.cliente,
            )
            session.add(factura)
            session.commit()

        return 1

    elif user.rol_id == 1 and user.estado:
        return 2

    elif user.rol_id == 2 and user.estado:
        return 3

    elif not user.estado:
        return 4

    else:
        return 5
