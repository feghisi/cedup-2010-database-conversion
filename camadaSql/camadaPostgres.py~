# -*- coding: iso-8859-1 -*-
__author__='Fernando Ghisi'

class CamadaSQL:
	def __init__(self, conexao):
		self.conexao = conexao.conexao
		self.cursor = conexao.cursor

	def open_file(self):
		arquivo = open("log_conversao.txt", "a")

		return arquivo

	def close_file(self, arquivo):
		arquivo.close()

	def insert(self, dados_dict, tabela):
		'''
		-> Parametros
			- dados_dict: Dicionario contendo campos necessario para o insert
			- tabela: Tabela que sera inseridas os dados
		'''
		
		campos = []
		values = []
		arquivo_log = self.open_file()

		for chave, value in dados_dict.items():
			value = str(value)
			
			# TODO: rever essa gambiarra
			if not value or value == 'None':
				continue
			
			campos.append(chave)
			values.append(value)
		
		try:
			sql = "insert into %s (%s) values ('%s')" % (tabela, ",".join(campos), "','".join(values))
		except:
			return True
		
		print sql

		try:
			self.cursor.execute(sql)
			arquivo_log.write('%s\n' % sql)
		except Exception, e:
			arquivo_log.write(str(e))
			self.conexao.rollback()
			print 'Traceback: %s' % str(e)
			print "Erro interno ao inserir na tabela %s" % tabela
			print "Instrucao SQL: ", sql
			return False
		
		self.close_file(arquivo_log)
		self.conexao.commit()
		return True

	def update(self, tabela, campos_dict, where_list):
		'''
		-> Parametros
			- campos_dict: Dicionario contendo campos necessario com seus valores para o update
			- tabela: Tabela que sera atualiza os dados
			- where_list: Condição para o update
		'''
		
		sql_update = []

		for chave, value in campos_dict.items():
			sql_update.append("%s = '%s'" % (chave, value)) 
		
		if where_list:
			where = " and ".join(where_list)
			
			sql = "update %s set %s where %s" % (tabela, ",".join(sql_update), where)
		else:
			sql = "update %s set %s" % (tabela, ",".join(sql_update))
		
		print sql
		try:
			self.cursor.execute(sql)
		except:
			print "Erro interno ao atualizar dados na tabela %s" % tabela
			print "Instrucao SQL: ", sql
			return False

		self.conexao.commit()
		return True

	def delete(self, tabela, where_list=None):
		'''
		-> Parametros
			- tabela: Tabela que sera excluido os registros
			- where_list: Condição para o delete
		'''

		if where_list:
			where = " and ".join(where_list)

			sql = "delete from %s where %s" % (tabela, where)
		else:
			sql = "delete from %s"
		
		print sql
		try:
			self.cursor.execute(sql)
		except:
			print "Erro interno ao deletar dados na tabela %s" % tabela
			print "Instrucao SQL: ", sql
			return False

		self.conexao.commit()
		return True

	def select(self, tabela, campos_list, where_list=None):
		'''
		-> Parametros
			- campos_list: Lista contendo campos necessario para a consulta
			- tabela: Tabela que sera realizada a consulta de dados
			- where_list: Condição para consulta
		'''

		campos = ",".join(campos_list)
		arquivo_log = self.open_file()
		
		if where_list:
			where = " and ".join(where_list)

			sql = "select %s from %s where %s" % (campos, tabela, where)
		else:
			sql = "select %s from %s" % (campos, tabela)

		arquivo_log.write('%s\n' % sql)

		self.close_file(arquivo_log)
		self.cursor.execute(sql)
		return self.cursor.fetchall()
	
	def __del__(self):
		del self		 
