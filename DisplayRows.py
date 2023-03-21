from nicegui import ui
from Sale import Sale


def short_str(string: str) -> str:
    if len(string) > 15:
        return string[:15:] + '...'
    else:
        return string


class DisplayRow(ui.row):
    def __init__(self, sale: Sale, row):
        super().__init__()
        container = ui.row().classes('width:100% items-center justify-between mx-auto')
        pending = sale.get_status()
        with container:
            ui.label(str(row + 1)).style('width: 35px')
            with ui.expansion('Items', icon='book').classes('w-auto').style('width: 400px'):
                for item in sale.products:
                    with ui.row().classes('items-center justify-between'):
                        ui.label(short_str(item.title)).classes('mr-12 col-start-auto').style('width: 150px')
                        ui.label(item.state.upper()).classes('mr-8 text-center').style('width: 50px')
                        ui.label(str(item.price)).classes('mr-8 text-center').style('width: 50px')
            ui.label(sale.payment_method.upper()).classes('mx-32').style('width: 80px')
            ui.label(str(sale.total)).style('width: 128px')

            def create_invoice():
                if sale.create_invoice():
                    container.remove(-1)
                    container.remove(-1)
                    with container:
                        ui.icon('check').classes('mx-8')
            ui.button('Create Invoice', on_click=lambda: create_invoice()).classes('mr-8')
            if pending:
                ui.icon('check').classes('mx-8')
            else:
                ui.icon('close').classes('mx-8')



    def done_pending(self, done=False):
        with ui.container():
            pass
