from fastapi import FastAPI
from nicegui import ui
from datetime import date

from Invoicer import Invoicer
from DisplayRows import DisplayRow


def init(app: FastAPI, invoicer: Invoicer) -> None:
    @ui.page('/')
    def show():
        ui.label('Welcome to El Rio Software Invoice Microservice!')

    @ui.page('/invoices/')
    async def invoice_page():
        sales = await invoicer.get_sales()
        print(len(sales))
        row = 0
        for num, sale in enumerate(sales):
            DisplayRow(sale, num)
            row += 1

    ui.run_with(app)
