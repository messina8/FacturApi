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
        with ui.header(elevated=True).style('background-color: #0e3c45') \
                .classes('items-center justify-between') \
                .style('box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1)'):
            with ui.row().classes('items-center justify-between'):
                ui.button(on_click=lambda: left_drawer.toggle()).props('flat color=white icon=menu')
                ui.label('El Rio Software').style('color: #hhhhhh').classes('font-serif')
            ui.button().props('flat color=white icon=add')
            ui.button().props('flat color=white icon=home')
            with ui.left_drawer(value=False, top_corner=False, bottom_corner=True).style('background-color: #0e3c45') as left_drawer:
                ui.label('LEFT DRAWER').style('color: #hhhhhh').classes('font-serif')

        with column:
            for num, sale in enumerate(sales):
                DisplayRow(sale, num)
                row += 1
            NewSale(invoicer)

        async def refresh():
            column.update()

        ui.timer(0.1, refresh)

    @ui.page('/test_page')
    async def test_page():
        ui.label('CONTENT')
        [ui.label(f'Line {i}') for i in range(100)]
        with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
            ui.label('HEADER')
            ui.button(on_click=lambda: right_drawer.toggle()).props('flat color=white icon=menu')
        with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
            ui.label('LEFT DRAWER')
        with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as right_drawer:
            ui.label('RIGHT DRAWER')
        with ui.footer().style('background-color: #3874c8'):
            ui.label('FOOTER')

    ui.run_with(app)
