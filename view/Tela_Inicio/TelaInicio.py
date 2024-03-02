from kivymd.uix.screen import MDScreen
from plyer import filechooser
from config import image_source, texto
import cv2
import pytesseract
from view.Tela_Carregamento_IA.TelaCarregamentoIA import *
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton

class TelaInicioView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def file_chooser(self):
        try:
            if self.selected:
                filechooser.open_file(on_selection=self.selected)
                img = cv2.imread(self.ids.img.source)
                pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"
                resultado = pytesseract.image_to_string(img)
                texto[0] = resultado
                print(resultado)
            else:
                self.dialog = MDDialog(
                    title="Erro",
                    size=(400, 400),
                    size_hint=(None, None),
                    text="Tente novamente.",
                    buttons=[MDRectangleFlatButton(text="Ok", on_release=self.liberar)])
                self.dialog.open()
        except:
            self.dialog = MDDialog(
                title="Erro",
                size=(400, 400),
                size_hint=(None, None),
                text="Tente novamente.",
                buttons=[MDRectangleFlatButton(text="Ok", on_release=self.liberar)])
            self.dialog.open()

    def liberar(self, obj):
        self.dialog.dismiss()
    def selected(self, selection):
        if selection:
            image_source[0] = selection[0]
            self.ids.img.source = selection[0]
            self.ids.text_img.text = selection[0]
    def sair(self):
        image_source[0] = ""
        self.ids.img.source = ""
        self.ids.text_img.text = ""
