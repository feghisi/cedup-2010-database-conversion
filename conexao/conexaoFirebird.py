# -*- coding: iso-8859-1 -*-
__author__='Fernando Ghisi'

import kinterbasdb

class ConnectFirebird:
	def __init__(self, db):
		try:
			# Metodo Connect (dns='c:/base.gdb', user='SYSDBA', password='masterkey')
			
			conn = kinterbasdb.connect(**db)
			self.conexao = conn
			self.cursor = conn.cursor()

		except:
			self.conexao = False
			print 'Erro ao se conectar ao banco de dados Postgres'

	def __del__(self):
		del self
