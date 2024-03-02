from kivymd.uix.screen import MDScreen
from config import image_source, mailUser
from DB import FirebaseP

FP = FirebaseP()
class TelaArquivoView(MDScreen):
    def on_enter(self):
            self.ids.img.source = image_source[0]
            FP.SendFile(mailUser[0], self.ids.img.source)