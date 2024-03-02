from kivymd.uix.screen import MDScreen

from config import texto

class TelaApresentacaoView(MDScreen):
    def on_enter(self):
        self.ids.text.text = texto[0]
    pass