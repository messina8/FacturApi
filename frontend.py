from fastapi import FastAPI
from nicegui import ui
from datetime import date

from Invoicer import Invoicer


def init(app: FastAPI, invoicer: Invoicer) -> None:
    # @ui.page('/')
    # def show():
    #     ui.label('Welcome to El Rio Software Invoice Microservice!')

    @ui.page('/invoices/')
    async def invoice_page():
        sales = await invoicer.get_sales()
        for invoice in sales:
            done = 'pending' if not invoice.done else 'Done'
            with ui.row().classes('width: 100% center mx-auto'):
                with ui.expansion('Items', icon='book'):
                    for item in invoice.products:
                        with ui.row():
                            ui.label(item.title)
                            ui.label(item.price)
                ui.label(invoice.payment_method)
                ui.label(invoice.total).classes('h:center')
                ui.label(done)
                ui.button('Create Invoice').classes()

    ui.run_with(app)
