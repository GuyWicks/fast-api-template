from ast import Return
import re
from fastapi import APIRouter, Path, Query, Header, status
from typing import List, Optional, FrozenSet

from ..models.model import MyClass

router = APIRouter()

#
#
#


@router.get(
    path="/",
    tags=["tag"],
    description="""
Description of the API endpoint
""",
    response_model=MyClass,
    response_description="""
Response description
""",
)
async def read_resource():
    return
