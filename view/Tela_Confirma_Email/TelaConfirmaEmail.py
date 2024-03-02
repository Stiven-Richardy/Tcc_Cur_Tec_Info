from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from random import randint
from emailSMT import servidorEmail
from config import mailUser
from config import nomeUser
from config import senhaUser
from config import msgErro
from datetime import date
from DB import FirebaseP
FP = FirebaseP()

def numeroRandom():
    ram = randint(10000, 99999)
    return ram

def confirmaUsuario(self):
    if(senhaUser[0] != ""):
        if (FP.Cadastro(mailUser[0], senhaUser[0], nomeUser[0])):
            senhaUser[0] = ""
            validForm(self, "Usuário cadastrado com sucesso!")
            return True
        else:
            if(msgErro[0] != ""):
                invalidFormCreateUser(self, msgErro[0])
            else:
                invalidFormCreateUser(self, 'Usuário já cadastrado no sistema!')
            return False

class TelaConfirmaEmailView(MDScreen):
    emailUser = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global valor
        valor = numeroRandom()

    def on_send(self):
        global valor
        servidorEmail().construiEmail(valor, mailUser[0])

    def on_submit(self):
        global valor
        #servidorEmail().construiEmail(valor, mailUser[0])
        if (self.codMail.text == str(valor)):
            confirmaUsuario(self)
            self.codMail.text = ""
            return True
        else:
            invalidForm(self)
            self.manager.current = "s2"

    def liberar(self, obj):
        self.dialog.dismiss()

def invalidForm(self):
    self.dialog = MDDialog(
        title='Código inválido',
        size=(400, 400),
        text="Código digitado está incorreto, usuário não pôde ser cadastrado!",
        size_hint=(None, None),
        buttons=[
            MDRectangleFlatButton(text="Ok", on_release= self.liberar)])
    self.dialog.open()

def validForm(self, texto):
    self.dialog = MDDialog(
        title='Cadastro concluído!',
        size=(400, 400),
        text=texto,
        size_hint=(None, None),
        buttons=[
            MDRectangleFlatButton(text="Ok", on_release=self.liberar)])
    self.dialog.open()

def invalidFormCreateUser(self, texto):
    self.dialog = MDDialog(
        title='Informações Inválidas',
        size=(400, 400),
        text=texto,
        size_hint=(None, None),
        buttons=[
            MDRectangleFlatButton(text="Ok", on_release=self.liberar)])
    self.dialog.open()