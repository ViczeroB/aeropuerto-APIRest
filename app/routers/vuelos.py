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

@router.post("/", response_model=schemas.Vuelo)
def create_vuelo(vuelo: schemas.VueloCreate, db: Session = Depends(get_db)):
    return crud.create_vuelo(db=db, vuelo=vuelo)

@router.get("/{vuelo_id}", response_model=schemas.Vuelo)
def read_vuelo(vuelo_id: int, db: Session = Depends(get_db)):
    db_vuelo = crud.get_vuelo(db, vuelo_id=vuelo_id)
    if db_vuelo is None:
        raise HTTPException(status_code=404, detail="Vuelo not found")
    return db_vuelo