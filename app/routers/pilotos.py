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

@router.post("/", response_model=schemas.Piloto)
def create_piloto(piloto: schemas.PilotoCreate, db: Session = Depends(get_db)):
    return crud.create_piloto(db=db, piloto=piloto)

@router.get("/{piloto_id}", response_model=schemas.Piloto)
def read_piloto(piloto_id: int, db: Session = Depends(get_db)):
    db_piloto = crud.get_piloto(db, piloto_id=piloto_id)
    if db_piloto is None:
        raise HTTPException(status_code=404, detail="Piloto not found")
    return db_piloto