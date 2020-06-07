# -*- coding: iso-8859-1 -*-
__author__='Fernando Ghisi'

import psycopg2
import psycopg2.extras

class ConnectPostgres:
	def __init__(self, db):
		try:
			# Metodo Connect (host='localhost', database='autosystem', user='postgres', password='postgres')

			conn = psycopg2.connect(**db)
			self.conexao = conn
			self.cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

		except:
			self.conexao = False
			print 'Erro ao se conectar ao banco de dados Postgres'

	def __del__(self):
		del self
