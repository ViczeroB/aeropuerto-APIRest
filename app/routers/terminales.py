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

@router.post("/", response_model=schemas.Terminal)
def create_terminal(terminal: schemas.TerminalCreate, db: Session = Depends(get_db)):
    return crud.create_terminal(db=db, terminal=terminal)

@router.get("/{terminal_id}", response_model=schemas.Terminal)
def read_terminal(terminal_id: int, db: Session = Depends(get_db)):
    db_terminal = crud.get_terminal(db, terminal_id=terminal_id)
    if db_terminal is None:
        raise HTTPException(status_code=404, detail="Terminal not found")
    return db_terminal