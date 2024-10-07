from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.VehiculoAereo)
def create_vehiculo_aereo(vehiculo_aereo: schemas.VehiculoAereoCreate, db: Session = Depends(get_db)):
    return crud.create_vehiculo_aereo(db=db, vehiculo_aereo=vehiculo_aereo)

@router.get("/{vehiculo_aereo_id}", response_model=schemas.VehiculoAereo)
def read_vehiculo_aereo(vehiculo_aereo_id: int, db: Session = Depends(get_db)):
    db_vehiculo_aereo = crud.get_vehiculo_aereo(db, vehiculo_aereo_id=vehiculo_aereo_id)
    if db_vehiculo_aereo is None:
        raise HTTPException(status_code=404, detail="Vehiculo Aereo not found")
    return db_vehiculo_aereo