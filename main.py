from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from view.Tela_Login.TelaLogin import TelaLoginView
from view.Tela_Cadastro.TelaCadastro import TelaCadastroView
from view.Tela_Inicio.TelaInicio import TelaInicioView
from view.Tela_Contato.TelaContato import TelaContatoView
from view.Tela_Perfil.TelaPerfil import TelaPerfilView
from view.Tela_Arquivo.TelaArquivo import TelaArquivoView
from view.Tela_Carregamento_IA.TelaCarregamentoIA import TelaCarregamentoIAView
from view.Tela_Apresentacao.TelaApresentacao import TelaApresentacaoView
from view.Tela_Confirma_Email.TelaConfirmaEmail import TelaConfirmaEmailView
class MainApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)

        self.sm = MDScreenManager()

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.sm.add_widget(TelaLoginView())
        self.sm.add_widget(TelaCadastroView())
        self.sm.add_widget(TelaInicioView())
        self.sm.add_widget(TelaContatoView())
        self.sm.add_widget(TelaPerfilView())
        self.sm.add_widget(TelaArquivoView())
        self.sm.add_widget(TelaCarregamentoIAView())
        self.sm.add_widget(TelaApresentacaoView())
        self.sm.add_widget(TelaConfirmaEmailView())
        return self.sm
MainApp().run()
#self.sm.add_widget(TelaConfirmaEmailView())