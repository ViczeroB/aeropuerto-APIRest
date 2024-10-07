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

@router.post("/", response_model=schemas.Boleto)
def create_boleto(boleto: schemas.BoletoCreate, db: Session = Depends(get_db)):
    return crud.create_boleto(db=db, boleto=boleto)

@router.get("/{boleto_id}", response_model=schemas.Boleto)
def read_boleto(boleto_id: int, db: Session = Depends(get_db)):
    db_boleto = crud.get_boleto(db, boleto_id=boleto_id)
    if db_boleto is None:
        raise HTTPException(status_code=404, detail="Boleto not found")
    return db_boleto