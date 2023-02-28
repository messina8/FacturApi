from pydantic import BaseModel
from enum import Enum


class State(str, Enum):
    used = 'used'
    new = 'new'
    of = 'of'


class Product(BaseModel):
    title: str
    state: State
    supplier: str | None = None
    price: int
