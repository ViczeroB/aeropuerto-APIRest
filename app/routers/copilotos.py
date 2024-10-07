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

@router.post("/", response_model=schemas.Copiloto)
def create_copiloto(copiloto: schemas.CopilotoCreate, db: Session = Depends(get_db)):
    return crud.create_copiloto(db=db, copiloto=copiloto)

@router.get("/{copiloto_id}", response_model=schemas.Copiloto)
def read_copiloto(copiloto_id: int, db: Session = Depends(get_db)):
    db_copiloto = crud.get_copiloto(db, copiloto_id=copiloto_id)
    if db_copiloto is None:
        raise HTTPException(status_code=404, detail="Copiloto not found")
    return db_copiloto