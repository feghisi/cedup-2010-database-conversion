# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/interface.ui'
#
# Created: Sat May 28 20:11:32 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(744, 575)
        icon = QtGui.QIcon()

        icon.addPixmap(QtGui.QPixmap(_fromUtf8("interface/icone.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        MainWindow.setWindowIcon(icon)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.editor = Qsci.QsciScintilla(self.centralwidget)
        self.editor.setAcceptDrops(False)
        self.editor.setToolTip(_fromUtf8(""))
        self.editor.setWhatsThis(_fromUtf8(""))
        self.editor.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.editor.setAutoFillBackground(False)
        self.editor.setObjectName(_fromUtf8("editor"))
        self.gridLayout.addWidget(self.editor, 0, 0, 1, 1)
        self.columnView = QtGui.QColumnView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.columnView.sizePolicy().hasHeightForWidth())
        self.columnView.setSizePolicy(sizePolicy)
        self.columnView.setObjectName(_fromUtf8("columnView"))
        self.gridLayout.addWidget(self.columnView, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setSizeIncrement(QtCore.QSize(0, 0))
        self.toolBar.setBaseSize(QtCore.QSize(0, 0))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNovo = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/imagens/filenew-256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNovo.setIcon(icon1)
        self.actionNovo.setObjectName(_fromUtf8("actionNovo"))
        self.actionAbrir = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/imagens/fileopen-256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbrir.setIcon(icon2)
        self.actionAbrir.setObjectName(_fromUtf8("actionAbrir"))
        self.actionSalvar = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/imagens/filesave-256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalvar.setIcon(icon3)
        self.actionSalvar.setObjectName(_fromUtf8("actionSalvar"))
        self.actionSalvarComo = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/imagens/filesaveas-256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalvarComo.setIcon(icon4)
        self.actionSalvarComo.setObjectName(_fromUtf8("actionSalvarComo"))
        self.actionCompilar = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/imagens/artsbuilderexecute-256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCompilar.setIcon(icon5)
        self.actionCompilar.setObjectName(_fromUtf8("actionCompilar"))
        self.actionDebugar = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/imagens/compfile-256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDebugar.setIcon(icon6)
        self.actionDebugar.setObjectName(_fromUtf8("actionDebugar"))
        self.toolBar.addAction(self.actionNovo)
        self.toolBar.addAction(self.actionAbrir)
        self.toolBar.addAction(self.actionSalvar)
        self.toolBar.addAction(self.actionSalvarComo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCompilar)
        self.toolBar.addAction(self.actionDebugar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Debugres", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNovo.setText(QtGui.QApplication.translate("MainWindow", "Novo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNovo.setIconText(QtGui.QApplication.translate("MainWindow", "Novo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNovo.setToolTip(QtGui.QApplication.translate("MainWindow", "Novo(Ctrl+N)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNovo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbrir.setText(QtGui.QApplication.translate("MainWindow", "Abrir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbrir.setToolTip(QtGui.QApplication.translate("MainWindow", "Abrir(Ctrl+A)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbrir.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalvar.setText(QtGui.QApplication.translate("MainWindow", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalvar.setToolTip(QtGui.QApplication.translate("MainWindow", "Salvar(Ctrl+S)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalvar.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalvarComo.setText(QtGui.QApplication.translate("MainWindow", "SalvarComo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalvarComo.setIconText(QtGui.QApplication.translate("MainWindow", "Salvar...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalvarComo.setToolTip(QtGui.QApplication.translate("MainWindow", "Salvar Como(Ctrl+B)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalvarComo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+B", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompilar.setText(QtGui.QApplication.translate("MainWindow", "Compilar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompilar.setToolTip(QtGui.QApplication.translate("MainWindow", "Compilar(F9)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompilar.setShortcut(QtGui.QApplication.translate("MainWindow", "F9", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDebugar.setText(QtGui.QApplication.translate("MainWindow", "Debugar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDebugar.setToolTip(QtGui.QApplication.translate("MainWindow", "Debugar(F8)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDebugar.setShortcut(QtGui.QApplication.translate("MainWindow", "F8", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import Qsci
import icons_rc
