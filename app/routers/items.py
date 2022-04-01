from fastapi import APIRouter, Path, Query, Header, status, Depends
from typing import List, Optional, FrozenSet
from sqlalchemy.orm import Session

#from database.connection import SessionLocal, engine

from ..database import schemas, crud
from ..database.connection import get_db

router = APIRouter()

# Dependency


@router.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
