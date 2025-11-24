# esta es la base de todos los modelos, supuestamente le dice "che esto es una tabla"
from decimal import Decimal
from enum import auto
from pydantic import EmailStr
from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    Text,
    Date,
    String,
    Boolean,
    Time,
    ForeignKey,
    DateTime,
    null,
    Table,
)
from sqlalchemy.log import STACKLEVEL
from sqlalchemy.orm import foreign, relationship, declarative_base
from datetime import date, datetime

Base = declarative_base()


class Rol(Base):
    __tablename__ = "rol"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30), nullable=False)
    descripcion = Column(String(150), nullable=True)
    usuarios = relationship("Usuario", back_populates="rol")


class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150), nullable=False)
    apellidos = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    key = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    estado = Column(Boolean, nullable=False, default=True)
    rol_id = Column(Integer, ForeignKey("rol.id", ondelete="RESTRICT"), nullable=False)
    rol = relationship("Rol", back_populates="usuarios")
    pagos = relationship("Pago", back_populates="usuario")
    proyectos = relationship("Proyecto", back_populates="usuario")
    factura = relationship("Factura", back_populates="usuario")


class Pago(Base):
    __tablename__ = "pago"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_hora = Column(DateTime, default=datetime.now, nullable=False)
    usuario_id = Column(
        Integer, ForeignKey("usuario.id", ondelete="CASCADE"), nullable=False
    )
    usuario = relationship("Usuario", back_populates="pagos")
    concepto = Column(String(255), nullable=True)
    nit = Column(String(30), nullable=True)
    numero_factura = Column(Integer, unique=True, nullable=False)
    monto = Column(Numeric(10, 2), nullable=False)


class Proyecto(Base):
    __tablename__ = "proyecto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(
        Integer, ForeignKey("usuario.id", ondelete="CASCADE"), nullable=False
    )
    usuario = relationship("Usuario", back_populates="proyectos")
    nombre = Column(String(150), nullable=False)
    descripcion = Column(String(255), nullable=True)
    fecha_creacion = Column(Date, default=date.today)
    estado = Column(Boolean, default=True, nullable=False)
    eventos = relationship("Evento", back_populates="proyecto")
    etiquetas = relationship("Etiqueta", back_populates="proyecto")
    datos = relationship("Dato", back_populates="proyecto")
    notas = relationship("Nota", back_populates="proyecto")
    recursos = relationship("Recurso", back_populates="proyecto")
    enlaces = relationship("Enlace", back_populates="proyecto")


class Evento(Base):
    __tablename__ = "evento"

    id = Column(Integer, primary_key=True, autoincrement=True)
    proyecto_id = Column(
        Integer, ForeignKey("proyecto.id", ondelete="CASCADE"), nullable=False
    )
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=True)
    fecha_hora_creacion = Column(DateTime, default=datetime.now, nullable=False)
    fecha_hora_evento = Column(DateTime, default=datetime.now, nullable=True)
    recordatorio = Column(Boolean, default=True, nullable=False)
    proyecto = relationship("Proyecto", back_populates="eventos")
    tipo = Column(String(20), nullable=False)

    __mapper_args__ = {"polymorphic_identity": "evento", "polymorphic_on": tipo}


class Tarea(Evento):
    __tablename__ = "tarea"

    id = Column(Integer, ForeignKey("evento.id"), primary_key=True)
    # usar los rangos de importancia desde el programa
    importancia = Column(Integer, nullable=False, default=0)
    estado = Column(Boolean, default=False, nullable=False)

    __mapper_args__ = {"polymorphic_identity": "tarea"}


class TipoRecurso(Base):
    __tablename__ = "tipo_recurso"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(70), nullable=False)
    descripcion = Column(String(255))
    recursos = relationship("Recurso", back_populates="tipo")


class Recurso(Base):
    __tablename__ = "recurso"

    id = Column(Integer, primary_key=True, autoincrement=True)
    proyecto_id = Column(
        Integer, ForeignKey("proyecto.id", ondelete="CASCADE"), nullable=False
    )
    tipo_recurso_id = Column(
        Integer, ForeignKey("tipo_recurso.id", ondelete="RESTRICT")
    )
    nombre = Column(String(100), nullable=True)
    descripcion = Column(String(155), nullable=True)
    proyecto = relationship("Proyecto", back_populates="recursos")
    tipo = relationship("TipoRecurso", back_populates="recursos")
    relevancia = Column(Integer, nullable=True, default=0)
    fecha_creacion = Column(Date, nullable=False, default=date.today)
    url = Column(String(255))

    __mapper_args__ = {"polymorphic_identity": 2, "polymorphic_on": tipo_recurso_id}


class Libro(Recurso):
    __tablename__ = "libro"

    id = Column(Integer, ForeignKey("recurso.id"), primary_key=True)
    autor = Column(String(200), nullable=True)
    editorial = Column(String(100))
    nota = Column(String(255))
    path = Column(String(255))

    __mapper_args__ = {"polymorphic_identity": 1}


etiquetas_datos = Table(
    "etiquetas_datos",
    Base.metadata,
    Column("etiqueta_id", Integer, ForeignKey("etiqueta.id"), primary_key=True),
    Column("dato_id", Integer, ForeignKey("dato.id"), primary_key=True),
)


etiquetas_notas = Table(
    "etiquetas_notas",
    Base.metadata,
    Column("etiqueta_id", Integer, ForeignKey("etiqueta.id"), primary_key=True),
    Column("nota_id", Integer, ForeignKey("nota.id"), primary_key=True),
)


class Etiqueta(Base):
    __tablename__ = "etiqueta"

    id = Column(Integer, primary_key=True, autoincrement=True)
    proyecto_id = Column(
        Integer, ForeignKey("proyecto.id", ondelete="CASCADE"), nullable=False
    )
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(150))
    color = Column(String(10), nullable=False)
    proyecto = relationship("Proyecto", back_populates="etiquetas")
    datos = relationship("Dato", secondary=etiquetas_datos, back_populates="etiquetas")
    notas = relationship("Nota", secondary=etiquetas_notas, back_populates="etiquetas")


class Dato(Base):
    __tablename__ = "dato"

    id = Column(Integer, primary_key=True, autoincrement=True)
    proyecto_id = Column(Integer, ForeignKey("proyecto.id", ondelete="CASCADE"))
    proyecto = relationship("Proyecto", back_populates="datos")
    titulo = Column(String(150), nullable=False)
    contenido = Column(String(255))
    importancia = Column(Integer, nullable=True)
    fecha_creacion = Column(DateTime, default=datetime.now, nullable=False)
    etiquetas = relationship(
        "Etiqueta", secondary=etiquetas_datos, back_populates="datos"
    )


class Nota(Base):
    __tablename__ = "nota"

    id = Column(Integer, primary_key=True, autoincrement=True)
    proyecto_id = Column(Integer, ForeignKey("proyecto.id", ondelete="CASCADE"))
    proyecto = relationship("Proyecto", back_populates="notas")
    titulo = Column(String(150))
    contenido = Column(Text)
    fecha_creacion = Column(DateTime, default=datetime.now, nullable=False)
    etiquetas = relationship(
        "Etiqueta", secondary=etiquetas_notas, back_populates="notas"
    )


class Enlace(Base):
    __tablename__ = "enlace"

    id = Column(Integer, primary_key=True, autoincrement=True)
    proyecto_id = Column(Integer, ForeignKey("proyecto.id", ondelete="CASCADE"))
    proyecto = relationship("Proyecto", back_populates="enlaces")
    origen = Column(Integer, nullable=False)
    destino = Column(Integer, nullable=False)
    tipo_origen = Column(String(50), nullable=False)
    tipo_destino = Column(String(50), nullable=False)


class Factura(Base):
    __tablename__ = "factura"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(
        Integer, ForeignKey("usuario.id", ondelete="SET NULL"), nullable=True
    )
    usuario = relationship("Usuario", back_populates="factura", uselist=False)
    nit = Column(Integer, nullable=False)  # validar esto con pydantic
    fecha_hora = Column(DateTime, default=datetime.now, nullable=False)
    concepto = Column(
        String(255),
        default="Suscripción de usuario a producto de investigación",
        nullable=False,
    )
    monto = Column(Numeric(5, 2), nullable=False)
    correo_destino = Column(String(150))
    cliente = Column(String(255))  # el nombre del cliente de la factura
    codigos = relationship("Codigo", back_populates="factura", uselist=False)


class Codigo(Base):
    __tablename__ = "codigo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_hora = Column(DateTime, default=datetime.now)
    factura_id = Column(Integer, ForeignKey("factura.id", ondelete="CASCADE"))
    factura = relationship("Factura", back_populates="codigos")
    banco = Column(String(20), nullable=True)
    impuesto = Column(String(20), nullable=True)
    contab = Column(String(20), nullable=True)
