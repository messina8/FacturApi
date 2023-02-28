from datetime import date

from Product import Product
from Sale import Sale
from Purchase import Purchase


class Invoicer:
    def __init__(self):
        self.sales = []
        self.purchases = []

    async def get_sales(self):
        return self.sales

    async def mass_invoice_creation(self):
        for sale in self.sales:
            sale.facturate()

    async def new_venta(self, products_data: list[Product], payment_method, sale_date=date.today(), client_id=None,
                        email=None):
        products = []
        for p in products_data:
            products.append(p)
        venta = Venta(products, payment_method, sale_date, client_id, email)
        self.sales.append(venta)

    async def new_sale(self, sale: Sale):
        self.sales.append(sale)

    async def new_purchase(self, total: int, qty: int, client_name: str, client_address: str, client_id: int,
                           purchase_date=date.today()):
        purchase = Purchase(total=total, qty=qty, client_name=client_name, client_address=client_address,
                            client_id=client_id, purchase_date=purchase_date)
        self.purchases.append(purchase)
