#encoding: latin1
class Base:
	def setBase(self, QtGui, MainWindow):
		self.QtGui = QtGui
		self.MainWindow = MainWindow 

	def InformationMsg(self, msg):
		self.QtGui.QMessageBox.information(self.MainWindow, 'Debugres', msg)
		
	def CriticalMsg(self, msg):
		self.QtGui.QMessageBox.critical(self.MainWindow, 'Debugres', msg)

	def AboutMsg(self, msg):
		self.QtGui.QMessageBox.about(self.MainWindow, 'Debugres', msg)

	def WarningMsg(self, msg):
		self.QtGui.QMessageBox.warning(self.MainWindow, 'Debugres', msg)
