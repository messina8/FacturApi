from nicegui import ui
import requests

import Product
from Invoicer import Invoicer
from Sale import Sale, Payment
from Product import Product, State, Supplier


class ProductColumn(ui.row):
    def __init__(self, deletable=False):
        super().__init__()
        with ui.row():
            ui.input('Title', )
            ui.number('Price')
            ui.select([e.value for e in State])
            ui.select([e.value for e in Supplier] + [None], value=None)


class NewSale(ui.row):
    def __init__(self, invoicer: Invoicer):
        super().__init__()

        with ui.row().classes('width:100% center mx-auto'):
            products = ui.column()
            with ui.column():
                with products:
                    ProductColumn()

                def add_product_column():
                    with products:
                        ProductColumn(True)

                def remove_product_column():
                    products.remove(-1)

                ui.button('del', on_click=lambda: remove_product_column())
                ui.button('add', on_click=lambda: add_product_column())
        with ui.row():
            ui.input('Client ID')
            ui.select([e.value for e in Payment], value=Payment.cash)
            ui.input('e-mail')

            def create_sale():
                for i in products.slots:
                    print(i)

            ui.button('New Sale', on_click=lambda: create_sale())


class SaleDialog(ui.dialog):
    def __init__(self):
        super().__init__()
