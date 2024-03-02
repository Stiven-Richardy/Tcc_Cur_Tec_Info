from kivymd.uix.screen import MDScreen
from config import mailUser
from datetime import date
class TelaPerfilView(MDScreen):
    def on_enter(self):
        self.ids.text.text = mailUser[0]
        self.ids.data.text = date.today().strftime("%d/%m/%Y")
    pass