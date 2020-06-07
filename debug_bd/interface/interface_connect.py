#encoding: latin1
from interface import Ui_MainWindow
from evento_botao import EventoBotao

class InterfaceConnect:
	def __init__(self):
		self.ui = Ui_MainWindow()
		self.EB = EventoBotao(self.ui)

	def connect_sinal(self):
		self.EB.configure()

		#Conecta as ações aos botões da tela
		self.ui.actionNovo.pyqtConfigure(triggered=self.EB.__novo__)
		self.ui.actionAbrir.pyqtConfigure(triggered=self.EB.__abrir__)
		self.ui.actionSalvar.pyqtConfigure(triggered=self.EB.__salvar__)
		self.ui.actionSalvarComo.pyqtConfigure(triggered=self.EB.__salvar_como__)
		self.ui.actionCompilar.pyqtConfigure(triggered=self.EB.__compilar__)
		self.ui.actionDebugar.pyqtConfigure(triggered=self.EB.__debugar__)


