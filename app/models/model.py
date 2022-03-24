from pydantic import BaseModel, Field
from enum import Enum

class MyEnum(str, Enum):
    active = "ACTIVE"
    closed = "CLOSED"

class MyClass(BaseModel):
    link: int
    name: str
    