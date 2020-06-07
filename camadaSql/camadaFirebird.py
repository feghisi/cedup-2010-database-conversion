# -*- coding: iso-8859-1 -*-
__author__='Fernando Ghisi'

class CamadaSQL:
	def __init__(self, conexao):
		self.conexao = conexao.conexao
		self.cursor = conexao.cursor

	def insert(self):
		pass

	def update(self):
		pass

	def delete(self):
		pass

	def select(self):
		self.cursor.execute("select * from pessoa")
		return self.cursor.fetchall()

	def __del__(self):
		del self	
