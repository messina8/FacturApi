from datetime import date
from pydantic import BaseModel


class Purchase(BaseModel):
    total: int
    qty: int
    client_name: str
    client_address: str
    client_id: int
    purchase_date: date = date.today()
