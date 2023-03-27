from nicegui import ui
import frontend


class Header(ui.header):
    def __init__(self, home=True, home_page=None):
        super().__init__()
        self.style('background-color: #0e3c45').classes('items-center justify-between') \
            .style('box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1)')
        with self:
            with ui.row().classes('items-center justify-between'):
                ui.button(on_click=lambda: left_drawer.toggle()).props('flat color=white icon=menu')
                ui.label('El Rio Software').style('color: #hhhhhh').classes('font-serif')
            left_drawer = ui.left_drawer(value=False, top_corner=False, bottom_corner=True).style(
                'background-color: #0e3c45')
            if home:
                ui.button(on_click=lambda: ui.open('/')).props('flat color=white icon=home')
