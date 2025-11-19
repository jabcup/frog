from fastapi import APIRouter, HTTPException
from pydantic import HttpUrl
from sqlalchemy import select, and_
from sqlalchemy.exc import SQLAlchemyError
from app.schemas.user_schemas import UserCreate, LoginReq, LoginRes
from app.db.session import SessionLocal
from app.db.models import Usuario
from app.auth import create_access_token

router = APIRouter(tags=["users"])


@router.post("/create_user")
def create_user(user: UserCreate):
    user_to_add = Usuario(
        nombre=user.nombre,
        apellidos=user.apellidos,
        email=user.email,
        key=user.key,
        fecha_nacimiento=user.fecha_nacimiento,
        estado=1,
        rol_id=3,
    )
    try:
        with SessionLocal() as session:
            session.add(user_to_add)
            session.commit()
            session.refresh(user_to_add)  # esto obtiene el id recien insertado

    except SQLAlchemyError as e:
        print("error al insertar a la base de datos")
        raise HTTPException(status_code=500, detail=f"error al crear usuario: {str(e)}")

    # print(user)
    return user


@router.post("/login")
def get_user(user: LoginReq):
    try:
        with SessionLocal() as session:
            user_to_log = select(Usuario).where(
                and_(Usuario.email == user.email, Usuario.key == user.key)
            )
            user_to_log = session.scalar(user_to_log)

        if user_to_log is None:
            raise HTTPException(status_code=401, detail="Datos incorrectos")
        token = create_access_token(data={"sub": str(user_to_log.id)})
        return {"user": user_to_log, "access_token": token}
    except SQLAlchemyError as sae:
        print("Error en la base de datos: ", sae)
        raise HTTPException(status_code=500, detail="Error en la base de datos")

    except HTTPException:
        raise

    except Exception as exc:
        print("error encontrado: ", exc)
        raise HTTPException(
            status_code=500, detail="Error del servidor en endpoint getuser"
        )
