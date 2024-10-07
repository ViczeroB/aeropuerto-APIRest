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

@router.post("/", response_model=schemas.Avioneta)
def create_avioneta(avioneta: schemas.AvionetaCreate, db: Session = Depends(get_db)):
    return crud.create_avioneta(db=db, avioneta=avioneta)

@router.get("/{avioneta_id}", response_model=schemas.Avioneta)
def read_avioneta(avioneta_id: int, db: Session = Depends(get_db)):
    db_avioneta = crud.get_avioneta(db, avioneta_id=avioneta_id)
    if db_avioneta is None:
        raise HTTPException(status_code=404, detail="Avioneta not found")
    return db_avioneta