from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.button import MDRectangleFlatButton
from view.Tela_Inicio.TelaInicio import TelaInicioView
from config import mailUser
from DB import FirebaseP

import os

MainWindow = TelaInicioView
class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


FP = FirebaseP()

def cadastroUser(self):
    print(os.getcwd())
    with cd(os.getcwd()):
        Builder.unload_file("my.kv")

        """self.current = "create"
        Builder.load_file('my.kv')"""

class TelaLoginView(MDScreen):
    def loginBtn(self):
        if FP.Login(self.email.text, self.senha.text):
            MainWindow.current = self.email.text
            mailUser[0] = self.email.text
            self.reset()
            return True
        else:
            invalidLogin(self)
            return False

    def createBtn(self):
        self.reset()
        cadastroUser(self)

    def reset(self):
        self.email.text = ""
        self.senha.text = ""
    def liberar(self, obj):
        self.dialog.dismiss()

def invalidLogin(self):
    self.dialog = MDDialog(
    title="Login Inválido",
    size=(400,400),
    size_hint=(None, None),
    text="Email ou senha inválidos",
    buttons=[
        MDRectangleFlatButton(text="Ok", on_release= self.liberar)])
    self.dialog.open()