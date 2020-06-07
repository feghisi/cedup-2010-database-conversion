from PyQt4.uic import compileUi

nome_arq = raw_input("Digite o nome do arquivo: ")
uifile = open("%s.ui" % nome_arq, "r")
pyfile = open("%s.py" % nome_arq, "w")

compileUi(uifile, pyfile)

uifile.close()
pyfile.close()

