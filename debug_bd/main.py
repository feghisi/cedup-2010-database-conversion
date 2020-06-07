#encoding: latin1
import sys
from PyQt4 import QtGui
from interface.interface_connect import InterfaceConnect

class Main(InterfaceConnect):
	def show(self):
		app = QtGui.QApplication(sys.argv)
		window = QtGui.QMainWindow()
		
		self.ui.setupUi(window)

		#Chama método da classe InterfaceConnect para conectar os eventos dos botões
		self.connect_sinal()
	
		window.show()
		sys.exit(app.exec_())

if __name__ == "__main__":
	Main().show()
