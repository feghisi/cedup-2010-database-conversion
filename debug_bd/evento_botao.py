#encoding: latin1
from PyQt4 import QtGui
from conexao import Conexao
from base import Base

class EventoBotao(Base):
	def __init__(self, ui):
		self.ui = ui
		self.filename = None
		self.Con = Conexao()
	
	def configure(self):
		self.setBase(QtGui, self.ui.MainWindow)
	
	def __novo__(self):
		self.ui.editor.setText("")
		self.filename = None

	def __abrir__(self):
		filename = unicode(QtGui.QFileDialog.getOpenFileName(self.ui.MainWindow, 'Abrir Arquivo', ''))
		if filename:
			fname = open(filename, 'r')
			data = fname.readlines()
			data = "".join(data)
			self.ui.editor.setText(data)
			self.filename = filename

	def __salvar_arquivo__(self, title, filename=None):
		'''
			Método genérico para salvar arquivo. Será utilizado no método __salvar__ 
			e no método __salvar_como__
		'''
		if not filename:
			filename = unicode(QtGui.QFileDialog.getSaveFileName(self.ui.MainWindow, title, ''))
			if not filename:
				return

		fname = open(filename, 'w')
		fname.write(self.ui.editor.text())
		fname.close()

		self.InformationMsg('Arquivo salvo com sucesso!')

		return filename

	def __salvar__(self):
		self.filename = self.__salvar_arquivo__('Salvar...', self.filename)
	
	def __salvar_como__(self):
		self.filename = self.__salvar_arquivo__('Salvar Como...')

	def __compilar__(self):
		QtGui.QMessageBox.information(self.ui.MainWindow, 'Debugres', 'Query compilada com sucesso!')
		self.Con.execute_bd(self.ui.editor.text())

	def __debugar__(self):
		print "CLICOU NO BOTAO DEBUGAR"

