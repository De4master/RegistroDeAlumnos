from sqlalchemy import Column, Integer, String
from app.database.conexion import Base

class Alumno(Base):
    __tablename__ = "alumnos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)
    correo = Column(String, unique=True, index=True, nullable=False)
    direccion = Column(String, nullable=False)  # ✅ Nuevo campo
