from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from config import mailUser
from config import nomeUser
from config import senhaUser
from DB import FirebaseP
FP = FirebaseP()

def enviaEmail(self):
    self.dialog = MDDialog(
        title='Digite o código enviado',
        size=(400, 400),
        text= "Código enviado: ",
        size_hint=(None, None),
        buttons=[
            MDTextField(hint_text="Teste"),
            MDRectangleFlatButton(text="Confirmar", on_release=self.liberar)])
    self.dialog.open()

def camposVazios(self):
    if (self.namee.text != "") and (self.email.text != "") and (self.email.text != ""):
        return True
    else:
        invalidForm(self, 'Preencha todos os campos!')
    return False

def confirmaSenha(self):
    if (self.password_confirm.text != ""):
        return True
    else:
        invalidForm(self, 'Repita a senha para confirmação!')
        return False

def senhasIguais(self):
    if (self.password_confirm.text == self.password.text):
        return True
    else:
        invalidForm(self, 'Senhas diferentes!')
        return False

def confirmaEmail(self):
    if self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
        return True
    else:
        invalidForm(self, 'Digite um e-mail válido!')
        return False


class TelaCadastroView(MDScreen):
    def submit(self):
        mailUser[0] = self.email.text
        nomeUser[0] = self.namee.text
        senhaUser[0] = self.password.text

        if (camposVazios(self) == True) and (confirmaSenha(self) == True) and (confirmaEmail(self) == True and (senhasIguais(self) == True)):
            self.manager.current = "sMail"
            self.reset()
            #root.manager.current = "sMail"
            #Deixar o retorno como True depois!  and (confirmaUsuario(self) == True)
            return True
        else:
            return False

    def login(self):
        self.reset()

    def liberar(self, obj):
        self.dialog.dismiss()

    def reset(self):
        self.namee.text = ""
        self.email.text = ""
        self.password.text = ""
        self.password_confirm.text = ""

def invalidForm(self, texto):
    self.dialog = MDDialog(
        title='Informações Inválidas',
        size=(400, 400),
        text=texto,
        size_hint=(None, None),
        buttons=[
            MDRectangleFlatButton(text="Ok", on_release=self.liberar)])
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
