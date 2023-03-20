from fastapi import FastAPI
from nicegui import ui, Client
from datetime import date
import time

from Invoicer import Invoicer
from DisplayRows import DisplayRow
from NewSale import NewSale


def init(app: FastAPI, invoicer: Invoicer) -> None:
    @ui.page('/')
    def show():
        ui.label('Welcome to El Rio Software Invoice Microservice!')

    @ui.page('/invoices/')
    async def invoice_page():
        sales = await invoicer.get_sales()
        print(len(sales))
        row = 0
        column = ui.column().classes('width:100% center mx-auto')
        with column:
            for num, sale in enumerate(sales):
                DisplayRow(sale, num)
                row += 1
            NewSale(invoicer)

        async def refresh():
            column.update()
        ui.timer(0.1, refresh)

    @ui.page('/test_page')
    async def test_page(client: Client):
        async def check():
            if await ui.run_javascript('window.pageYOffset >= document.body.offsetHeight - 2 * window.innerHeight'):
                ui.image(f'https://picsum.photos/640/360?{time.time()}')

        await client.connected()
        ui.timer(0.1, check)

    ui.run_with(app)
