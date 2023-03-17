import dataclasses
from datetime import date
from enum import Enum


from pydantic import BaseModel, ValidationError, validator
from pydantic.dataclasses import dataclass, Field
from Product import Product


class Payment(str, Enum):
    cash = 'cash'
    credit = 'credit'
    digital = 'MP'


@dataclass
class Sale:
    products: list[Product]
    payment_method: Payment
    client_id: int = None
    date: str | None = str(date.today())
    email: str | None = None
    done: bool | None = False
    invoice_number: int | None = None
    total: int = Field(..., init=False)

    def __post_init__(self):
        total = 0
        for product in self.products:
            total += product['price']
        self.total = total

    def create_invoice(self):
        if not self.done:
            # llamar a la API
            # mandar el mail desde el facturador
            print('Calling Tango API')
            self.invoice_number = None  # debería volver con la llamada a la API
            self.done = True

    def send_mail(self):
        if self.done:
            # mandar el mail lol
            pass

    def get_status(self):
        return self.done
