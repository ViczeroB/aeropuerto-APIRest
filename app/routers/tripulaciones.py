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

@router.post("/", response_model=schemas.Tripulacion)
def create_tripulacion(tripulacion: schemas.TripulacionCreate, db: Session = Depends(get_db)):
    return crud.create_tripulacion(db=db, tripulacion=tripulacion)

@router.get("/{tripulacion_id}", response_model=schemas.Tripulacion)
def read_tripulacion(tripulacion_id: int, db: Session = Depends(get_db)):
    db_tripulacion = crud.get_tripulacion(db, tripulacion_id=tripulacion_id)
    if db_tripulacion is None:
        raise HTTPException(status_code=404, detail="Tripulacion not found")
    return db_tripulacion