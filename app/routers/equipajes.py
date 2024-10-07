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

@router.post("/", response_model=schemas.Equipaje)
def create_equipaje(equipaje: schemas.EquipajeCreate, db: Session = Depends(get_db)):
    return crud.create_equipaje(db=db, equipaje=equipaje)

@router.get("/{equipaje_id}", response_model=schemas.Equipaje)
def read_equipaje(equipaje_id: int, db: Session = Depends(get_db)):
    db_equipaje = crud.get_equipaje(db, equipaje_id=equipaje_id)
    if db_equipaje is None:
        raise HTTPException(status_code=404, detail="Equipaje not found")
    return db_equipaje