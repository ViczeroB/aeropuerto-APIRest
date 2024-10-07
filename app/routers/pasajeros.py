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

@router.post("/", response_model=schemas.Pasajero)
def create_pasajero(pasajero: schemas.PasajeroCreate, db: Session = Depends(get_db)):
    return crud.create_pasajero(db=db, pasajero=pasajero)

@router.get("/{pasajero_id}", response_model=schemas.Pasajero)
def read_pasajero(pasajero_id: int, db: Session = Depends(get_db)):
    db_pasajero = crud.get_pasajero(db, pasajero_id=pasajero_id)
    if db_pasajero is None:
        raise HTTPException(status_code=404, detail="Pasajero not found")
    return db_pasajero