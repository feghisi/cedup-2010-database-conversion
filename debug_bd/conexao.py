#encoding: latin1
from psycopg2.extras import DictCursor 
from psycopg2 import connect

class Conexao:
	def __init__(self):
		self.con = connect(host="localhost", database="teste1", user="postgres", password="postgres")
		self.dbcur = self.con.cursor(cursor_factory=DictCursor)
	
	def execute_bd(self, sql):
		try:
			self.dbcur.execute(str(sql))
			#l = self.dbcur.fetchall()
		except:
			print "ERRO AO EXECUTAR"
			self.dbcur.rollback()
			return 

		print "EXECUTADO COM SUCESSO"
		return None


if __name__ == "__main__":
	Conexao().execute_bd("select * from cidade")
