import reflex as rx
from sqlalchemy import Column, LargeBinary
import sqlmodel

class Imagen(rx.Model, table=True):
    nombre: str
    # Usamos LargeBinary con un tamaño grande para soportar archivos pesados
    datos: bytes = sqlmodel.Field(
        sa_column=Column(LargeBinary(length=(2**32)-1))
    )
    tipo: str # Para guardar si es 'image/jpeg' o 'image/png'