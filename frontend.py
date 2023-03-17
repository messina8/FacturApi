from fastapi import FastAPI
from nicegui import ui
from datetime import date

from Invoicer import Invoicer


def short_str(string: str) -> str:
    if len(string) > 15:
        return string[:15:] + '...'
    else:
        return string


def init(app: FastAPI, invoicer: Invoicer) -> None:
    @ui.page('/')
    def show():
        ui.label('Welcome to El Rio Software Invoice Microservice!')

    @ui.page('/invoices/')
    async def invoice_page():
        sales = await invoicer.get_sales()
        for invoice in sales:
            with ui.row().classes('width: 100% center mx-auto'):
                with ui.expansion('Items', icon='book'):
                    for item in invoice.products:
                        with ui.row().classes('width: 256p'):
                            ui.label(short_str(item.title)).classes('width:128p')
                            ui.label(item.state).classes('width:8p')
                            ui.label(item.price).classes('width:8p')
                ui.label(invoice.payment_method).classes('width:32p')
                ui.label(invoice.total).classes('width:128p')
                if invoice.get_status():
                    ui.icon('check').classes('width:32p')
                ui.button('Create Invoice', on_click=invoice.create_invoice())

    ui.run_with(app)
