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
        self.container = ui.row().classes('width:100% center mx-auto').on('click', super().update())
        pending = sale.get_status()
        with self.container:
            ui.label(str(row + 1))
            with ui.expansion('Items', icon='book').classes():
                for item in sale.products:
                    with ui.row().classes('mx-auto'):
                        ui.label(short_str(item.title)).classes('mr-12 col-start-auto')
                        ui.label(item.state.upper()).classes('mr-8')
                        ui.label(str(item.price)).classes('mr-8 object-right')
            ui.label(sale.payment_method.upper()).classes('mx-32')
            ui.label(str(sale.total)).classes('width:128p')
            if pending:
                ui.icon('check').classes('mx-8')
            else:
                ui.icon('close').classes('mx-8')
            ui.button('Create Invoice', on_click=lambda: self.create_invoice(sale, self.container)).classes('mr-16')

    def create_invoice(self, sale, container):
        if sale.create_invoice():
            super().update()

    def done_pending(self, done=False):
        with ui.container():
            pass
