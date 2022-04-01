from fastapi import APIRouter, Path, Query, Header, status, Depends
from typing import List, Optional, FrozenSet
from sqlalchemy.orm import Session

from ..database import crud
from ..models import user, item
from ..database.connection import get_db

router = APIRouter()


@router.post("/users/{user_id}/items/", response_model=item.Item)
def create_item_for_user(
    user_id: int, item: item.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=List[item.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
