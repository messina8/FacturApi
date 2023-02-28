from datetime import date
from enum import Enum

from pydantic import BaseModel
from Product import Product


class Payment(str, Enum):
    cash = 'cash'
    credit = 'credit'
    digital = 'MP'


class Sale(BaseModel):
    products: list[Product]
    client_id: int | None = None
    payment_method: Payment
    date: str | None = str(date.today())
    email: str | None = None
    done: bool | None = False
    invoice_number: int | None = None
    total: int | None = 0

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
