from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.conexion import SessionLocal
from app.schemas import alumno as schemas
from app.crud import alumno as crud_alumno

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.AlumnoOut])
def get_alumnos(db: Session = Depends(get_db)):
    return crud_alumno.obtener_todos(db)

@router.get("/{id}", response_model=schemas.AlumnoOut)
def get_alumno(id: int, db: Session = Depends(get_db)):
    alumno = crud_alumno.obtener_por_id(db, id)
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return alumno

@router.post("/", response_model=schemas.AlumnoOut)
def crear_alumno(alumno: schemas.AlumnoCreate, db: Session = Depends(get_db)):
    return crud_alumno.crear_alumno(db, alumno)

@router.put("/{id}", response_model=schemas.AlumnoOut)
def actualizar_alumno(id: int, datos: schemas.AlumnoUpdate, db: Session = Depends(get_db)):
    alumno_actualizado = crud_alumno.actualizar_alumno(db, id, datos)
    if not alumno_actualizado:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return alumno_actualizado

@router.delete("/{id}")
def eliminar_alumno(id: int, db: Session = Depends(get_db)):
    alumno_eliminado = crud_alumno.eliminar_alumno(db, id)
    if not alumno_eliminado:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return {"mensaje": "Alumno eliminado correctamente"}
