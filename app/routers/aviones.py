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

@router.post("/", response_model=schemas.Avion)
def create_avion(avion: schemas.AvionCreate, db: Session = Depends(get_db)):
    return crud.create_avion(db=db, avion=avion)

@router.get("/{avion_id}", response_model=schemas.Avion)
def read_avion(avion_id: int, db: Session = Depends(get_db)):
    db_avion = crud.get_avion(db, avion_id=avion_id)
    if db_avion is None:
        raise HTTPException(status_code=404, detail="Avion not found")
    return db_avion