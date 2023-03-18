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
        with ui.row().classes('width:100% center mx-auto'):
            ui.label(str(row + 1))
            with ui.expansion('Items', icon='book').classes():
                for item in sale.products:
                    with ui.row().classes('mx-auto'):
                        ui.label(short_str(item.title)).classes('mr-12 col-start-auto')
                        ui.label(item.state.upper()).classes('mr-8')
                        ui.label(str(item.price)).classes('mr-8 object-right')
            ui.label(sale.payment_method.upper()).classes('mx-32')
            ui.label(str(sale.total)).classes('width:128p')
            if sale.get_status():
                ui.icon('check').classes('mx-8')
            else:
                ui.icon('close').classes('mx-8')
            ui.button('Create Invoice', on_click=lambda: sale.create_invoice()).classes('mr-16')
