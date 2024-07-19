from sqlalchemy import Column, Integer, String, DateTime
from .conexion import Base

class Registr(Base):
    __tablename__ = "ingreso"
    idingreso = Column(Integer, primary_key = True, index = True)
    usuario = Column(String(255))
    contrasena = Column(String(500))
    correo_electronico = Column(String(255))