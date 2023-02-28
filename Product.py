from pydantic import BaseModel, Field
from enum import Enum


class State(str, Enum):
    used = 'used'
    new = 'new'
    of = 'of'


class Supplier(str, Enum):
    PLA = 'pla'
    SUD = 'sud'
    RIV = 'riv'
    VYR = 'vyr'


class Product(BaseModel):
    title: str
    state: State
    supplier: Supplier | None = None
    price: int = Field(..., gt=0)
