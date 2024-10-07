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

@router.post("/", response_model=schemas.Helicoptero)
def create_helicoptero(helicoptero: schemas.HelicopteroCreate, db: Session = Depends(get_db)):
    return crud.create_helicoptero(db=db, helicoptero=helicoptero)

@router.get("/{helicoptero_id}", response_model=schemas.Helicoptero)
def read_helicoptero(helicoptero_id: int, db: Session = Depends(get_db)):
    db_helicoptero = crud.get_helicoptero(db, helicoptero_id=helicoptero_id)
    if db_helicoptero is None:
        raise HTTPException(status_code=404, detail="Helicoptero not found")
    return db_helicoptero