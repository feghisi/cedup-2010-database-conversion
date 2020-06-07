# -*- coding: iso-8859-1 -*-
__author__='Fernando Ghisi'

import sys  

from PyQt4 import QtCore, QtGui  

from qt.mainConversionDataBase import Ui_conversionDataBase
from conexao.conexaoPostgres import ConnectPostgres
from camadaSql.camadaPostgres import CamadaSQL

class WinConversionDataBase(QtGui.QWidget,Ui_conversionDataBase):  
	def __init__(self):  
		QtGui.QWidget.__init__(self)  
		self.setupUi(self)
		self.objectConnections()
		self.conexaoPostgres = False
		self.conexaoPostgres2 = False

	def objectConnections(self):
		''''Sinais dos Botões'''

		self.ed_passwordP.setEchoMode(QtGui.QLineEdit.Password)
		self.ed_passwordP2.setEchoMode(QtGui.QLineEdit.Password)
                                
		self.connect(self.bt_fechar, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT('close()'))
		self.connect(self.bt_ok, QtCore.SIGNAL('clicked()'), self.bt_ok_clicked)
		self.connect(self.testconect_Postgres, QtCore.SIGNAL('clicked()'), self.testconect_Postgres_clicked)
		self.connect(self.testconect_Postgres2, QtCore.SIGNAL('clicked()'), self.testconect_Postgres2_clicked)
		self.connect(self.bt_campos1, QtCore.SIGNAL('clicked()'), self.bt_campos1_clicked)
		self.connect(self.bt_campos2, QtCore.SIGNAL('clicked()'), self.bt_campos2_clicked)

	def bt_ok_clicked(self):
		if self.conexaoPostgres and self.conexaoPostgres2:
			campos_TreeView_Banco1 = self.get_dados_TreeView(self.modeloTreeViewBanco1, self.camposTabelaBanco1)
			campos_TreeView_Banco2 = self.get_dados_TreeView(self.modeloTreeViewBanco2, self.camposTabelaBanco2)

			if not self.processar_dados(campos_TreeView_Banco1, campos_TreeView_Banco2):
				QtGui.QMessageBox.critical(None, "MessageBox",  "Ocorreu erro ao converter dados")
			else:
				QtGui.QMessageBox.information(None, "MessageBox",  "Conversão de dados com sucesso!")
		else:
			QtGui.QMessageBox.critical(None, "MessageBox",  "Você precisa configurar a conexão com o Banco de Dados")

	def get_dados_TreeView(self, modelo, campos):
		treeviewList = []
		rowDict = {}

		for i in range(len(campos)):
			column1 = modelo.item(i, 0)
			column2 = modelo.item(i, 1)
			
			if column1:
				indice = ("%s") % column1.text()
				campo = ("%s") % column2.text()
				rowDict[indice] = campo
			else:
				continue
			
			treeviewList.append(rowDict)
			rowDict = {}

		return treeviewList

	def processar_dados(self, lista1, lista2):
		dlg = Dialog('Aguarde a conversão de dados...')
		dlg.show()

		campos_list = self.mapeamento_banco(lista1, lista2)
		dadosBD1_list = self.camadaSQLPostgres.select(self.combo_Banco1.currentText(), campos_list)
	
		tamanho_listDados = len(dadosBD1_list)
		for i in range(len(dadosBD1_list)):
			
			if not self.camadaSQLPostgres2.insert(dadosBD1_list[i], self.combo_Banco2.currentText()):
				return False

			dlg.progressBar.setRange(1, tamanho_listDados)
			dlg.progressBar.setValue(i)

		return True
		
	def mapeamento_banco(self, lista1, lista2):
		'''Mapeamento dos nomes dos campos entre os dois Banco de Dados'''

		map_campos = []

		for bd1 in lista1:
			for bd2 in lista2:
				for k1, v1 in bd1.items():
					for k2, v2 in bd2.items():
						if k1 and k2:
							if k1 == k2:
								string = "%s as %s" % (v1, v2)
								map_campos.append(string)

		return map_campos
		
	def testconect_Postgres_clicked(self):
		'''Configuração da conexão com o banco de dados Postgres (Extraindo)'''
		conexao = {}
		 
		conexao['host'] = ("%s") % self.ed_host.text()
		conexao['database'] = ("%s") % self.ed_database.text()
		conexao['user'] = ("%s") % self.ed_userP.text()
		conexao['password'] = ("%s") % self.ed_passwordP.text()
		self.escreve_arquivo_configuracao_conexao('E', conexao)
		
		self.conexaoPostgres = ConnectPostgres(conexao)
		
		if self.conexaoPostgres.conexao:
			self.camadaSQLPostgres = CamadaSQL(self.conexaoPostgres)
			tabelas_dict = self.get_nome_tabelas_Postgres('E')
			tabelas_list = self.return_lista(tabelas_dict)
			tabelas_list.sort()
			self.combo_Banco1.addItems(tabelas_list)

			QtGui.QMessageBox.information(None, "MessageBox",  "Conexão com sucesso!")
		else:
			QtGui.QMessageBox.critical(None, "MessageBox",  "Falha na conexão!")
			self.ed_host.setFocus()
	
	def testconect_Postgres2_clicked(self):
		'''Configuração da conexão com o banco de dados Postgres (Inserindo)'''
		conexao = {}
		 
		conexao['host'] = ("%s") % self.ed_host2.text()
		conexao['database'] = ("%s") % self.ed_database2.text()
		conexao['user'] = ("%s") % self.ed_userP2.text()
		conexao['password'] = ("%s") % self.ed_passwordP2.text()
		self.escreve_arquivo_configuracao_conexao('I', conexao)
		
		self.conexaoPostgres2 = ConnectPostgres(conexao)
		
		if self.conexaoPostgres2.conexao:
			self.camadaSQLPostgres2 = CamadaSQL(self.conexaoPostgres2)
			tabelas_dict = self.get_nome_tabelas_Postgres('I')
			tabelas_list = self.return_lista(tabelas_dict)
			tabelas_list.sort()
			self.combo_Banco2.addItems(tabelas_list)

			QtGui.QMessageBox.information(None, "MessageBox",  "Conexão com sucesso!")
		else:
			QtGui.QMessageBox.critical(None, "MessageBox",  "Falha na conexão!")
			self.ed_host2.setFocus()

	def bt_campos1_clicked(self):
		if self.combo_Banco1.currentText():
			campos_tabela = self.get_campos_tabelas_Postgres(self.combo_Banco1.currentText(), 'E')
			self.camposTabelaBanco1 = self.return_lista(campos_tabela)

			self.modeloTreeViewBanco1 = QtGui.QStandardItemModel()
			self.add_Items_TreeView(self.modeloTreeViewBanco1, self.camposTabelaBanco1)
			self.tv_Banco1.setModel(self.modeloTreeViewBanco1)

	def bt_campos2_clicked(self):
		if self.combo_Banco2.currentText():
			campos_tabela = self.get_campos_tabelas_Postgres(self.combo_Banco2.currentText(), 'I')
			self.camposTabelaBanco2 = self.return_lista(campos_tabela)

			self.modeloTreeViewBanco2 = QtGui.QStandardItemModel()
			self.add_Items_TreeView(self.modeloTreeViewBanco2, self.camposTabelaBanco2)
			self.tv_Banco2.setModel(self.modeloTreeViewBanco2)

	def get_nome_tabelas_Postgres(self, flag):
		campos = ['relname']
		where = ["relkind = 'r'"] 

		if flag == 'E':		
			return self.camadaSQLPostgres.select('pg_class', campos, where)
		else:
			return self.camadaSQLPostgres2.select('pg_class', campos, where)

	def get_campos_tabelas_Postgres(self, tabela, flag):
		campos = ['attname', "'' as editar"]
		where = ["attrelid = (select oid from pg_class where relname='%s') and attnum > 0 order by attnum" % tabela]

		if flag == 'E':
			return self.camadaSQLPostgres.select('pg_attribute', campos, where)
		else:
			return self.camadaSQLPostgres2.select('pg_attribute', campos, where)

	def return_lista(self, rs_tabelas):
		tabelas = []

		for t in rs_tabelas:
			for chave, value in t.items():
				tabelas.append(value)

		return tabelas

	def add_Items_TreeView(self, parent, elements):
		coluna_campos = []
		coluna_indice = []
		
		for text in elements:
			item = QtGui.QStandardItem(text)
			if text:
				coluna_campos.append(item)
			else:
				coluna_indice.append(item)
			
		parent.appendColumn(coluna_indice)
		parent.appendColumn(coluna_campos)

	def escreve_arquivo_configuracao_conexao(self, flag, conexao):
		arquivo = open("log_conversao.txt", "a")

		arquivo.write('#'*100)

		if flag == 'E':
			arquivo.write('\nExtraindo Dados do Banco.\n')
		else:
			arquivo.write('\nInserindo Dados no Banco.\n')

		arquivo.write('Host: %s\n' % conexao['host'])
		arquivo.write('DataBase: %s\n' % conexao['database'])
		arquivo.write('User: %s\n' % conexao['user'])
		arquivo.write('Password: %s\n' % conexao['password'])
		arquivo.write('#'*100)
		arquivo.write('\n')

		arquivo.close()

class Dialog(QtGui.QDialog):  
	def __init__(self, text, parent=None):
		super(Dialog, self).__init__(parent)
		self.label = QtGui.QLabel(text)
		self.progressBar = QtGui.QProgressBar()
		
		vbox = QtGui.QVBoxLayout() 
		vbox.addWidget(self.label)
		vbox.addWidget(self.progressBar)
		
		self.setWindowTitle('...')
		self.setLayout(vbox)
		
if __name__ == '__main__':  
	aplicativo = QtGui.QApplication(sys.argv)  
	Win = WinConversionDataBase()  
	Win.show()  
	sys.exit(aplicativo.exec_()) 
	
	#----------------------------------------------------#
	# Configuracao de conexao de banco de dados Firebird #
	#----------------------------------------------------#

	#def testconect_Firebird_clicked(self):
	#	'''Configuração da conexão com o banco de dados Firebird'''
	#	conexao = {}

	#	conexao['dsn'] = ("%s") % self.ed_diretorio.text()
	#	conexao['user'] = ("%s") % self.ed_userF.text()
	#	conexao['password'] = ("%s") % self.ed_passwordF.text()
		
	#	self.conexaoFirebird = ConnectFirebird(conexao)
		
	#	if self.conexaoFirebird.conexao:
	#		QtGui.QMessageBox.information(None, "MessageBox",  "Conexão com sucesso!")
	#	else:
	#		QtGui.QMessageBox.critical(None, "MessageBox",  "Falha na conexão!")
	#		self.ed_diretorio.setFocus()

	#def bt_diretorio_clicked(self):
	#	fileName = QtGui.QFileDialog.getOpenFileName(None, 'Open file','.','GDB (*.gdb);;')
	#	self.ed_diretorio.setText(fileName)

