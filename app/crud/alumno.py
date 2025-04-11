from sqlalchemy.orm import Session
from app.models.alumno import Alumno
from app.schemas.alumno import AlumnoCreate, AlumnoUpdate

def obtener_todos(db: Session):
    return db.query(Alumno).all()

def obtener_por_id(db: Session, alumno_id: int):
    return db.query(Alumno).filter(Alumno.id == alumno_id).first()

def crear_alumno(db: Session, alumno: AlumnoCreate):
    nuevo_alumno = Alumno(**alumno.dict())
    db.add(nuevo_alumno)
    db.commit()
    db.refresh(nuevo_alumno)
    return nuevo_alumno

def actualizar_alumno(db: Session, alumno_id: int, datos: AlumnoUpdate):
    alumno = obtener_por_id(db, alumno_id)
    if alumno:
        for key, value in datos.dict().items():
            setattr(alumno, key, value)
        db.commit()
        db.refresh(alumno)
    return alumno

def eliminar_alumno(db: Session, alumno_id: int):
    alumno = obtener_por_id(db, alumno_id)
    if alumno:
        db.delete(alumno)
        db.commit()
    return alumno
