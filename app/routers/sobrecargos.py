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

@router.post("/", response_model=schemas.Sobrecargo)
def create_sobrecargo(sobrecargo: schemas.SobrecargoCreate, db: Session = Depends(get_db)):
    return crud.create_sobrecargo(db=db, sobrecargo=sobrecargo)

@router.get("/{sobrecargo_id}", response_model=schemas.Sobrecargo)
def read_sobrecargo(sobrecargo_id: int, db: Session = Depends(get_db)):
    db_sobrecargo = crud.get_sobrecargo(db, sobrecargo_id=sobrecargo_id)
    if db_sobrecargo is None:
        raise HTTPException(status_code=404, detail="Sobrecargo not found")
    return db_sobrecargo