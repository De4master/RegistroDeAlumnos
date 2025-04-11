from pydantic import BaseModel

class AlumnoBase(BaseModel):
    nombre: str
    apellido: str
    edad: int
    correo: str
    direccion: str

class AlumnoCreate(AlumnoBase):
    pass

class AlumnoUpdate(AlumnoBase):
    pass

class AlumnoOut(AlumnoBase):
    id: int

    class Config:
        orm_mode = True
