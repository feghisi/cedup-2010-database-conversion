from PyQt4.uic import compileUi

nome_arq = raw_input("Digite o nome do arquivo: ")

#Cria backup do arquivo de interface
pyfile    = open("%s.py" % nome_arq, "r").readlines()
pyfilebkp = open("%s_bkp.py" % nome_arq, "w").writelines(pyfile)

uifile    = open("%s.ui" % nome_arq, "r")
pyfile    = open("%s.py" % nome_arq, "w")

compileUi(uifile, pyfile)

uifile.close()
pyfile.close()

arq = open("%s.py" % nome_arq, "r")
lines = arq.readlines()
arq.close()
arq = open("%s.py" % nome_arq, "w")

troca = [
	('        MainWindow.setObjectName(_fromUtf8("MainWindow"))\n',
	 '        self.MainWindow = MainWindow\n\n        MainWindow.setObjectName("MainWindow")\n'),
    ('        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icone.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)\n', 
	 '\n        icon.addPixmap(QtGui.QPixmap(_fromUtf8("interface/icone.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)\n\n')
		]

linha = []
for l in lines:
	if troca[0][0] == l:
		l = troca[0][1]
	elif troca[1][0] == l:
		l = troca[1][1]

	linha.append(l)

arq.writelines(linha)
arq.close()
