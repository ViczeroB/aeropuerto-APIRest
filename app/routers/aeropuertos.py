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

@router.post("/", response_model=schemas.Aeropuerto)
def create_aeropuerto(aeropuerto: schemas.AeropuertoCreate, db: Session = Depends(get_db)):
    return crud.create_aeropuerto(db=db, aeropuerto=aeropuerto)

@router.get("/{aeropuerto_id}", response_model=schemas.Aeropuerto)
def read_aeropuerto(aeropuerto_id: int, db: Session = Depends(get_db)):
    db_aeropuerto = crud.get_aeropuerto(db, aeropuerto_id=aeropuerto_id)
    if db_aeropuerto is None:
        raise HTTPException(status_code=404, detail="Aeropuerto not found")
    return db_aeropuerto