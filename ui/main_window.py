# Form implementation generated from reading ui file 'LS_manager.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 542)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 32))
        self.menubar.setObjectName("menubar")
        self.menuSearchParticipant = QtWidgets.QMenu(parent=self.menubar)
        self.menuSearchParticipant.setEnabled(True)
        self.menuSearchParticipant.setObjectName("menuSearchParticipant")
        self.menuEditar_alumne = QtWidgets.QMenu(parent=self.menubar)
        self.menuEditar_alumne.setObjectName("menuEditar_alumne")
        self.menuDocumentaci = QtWidgets.QMenu(parent=self.menubar)
        self.menuDocumentaci.setObjectName("menuDocumentaci")
        MainWindow.setMenuBar(self.menubar)
        self.actionDescarregar_Documentaci = QtGui.QAction(parent=MainWindow)
        self.actionDescarregar_Documentaci.setEnabled(True)
        self.actionDescarregar_Documentaci.setObjectName("actionDescarregar_Documentaci")
        self.actionCanviar_correu = QtGui.QAction(parent=MainWindow)
        self.actionCanviar_correu.setObjectName("actionCanviar_correu")
        self.menuEditar_alumne.addAction(self.actionCanviar_correu)
        self.menuDocumentaci.addAction(self.actionDescarregar_Documentaci)
        self.menubar.addAction(self.menuSearchParticipant.menuAction())
        self.menubar.addAction(self.menuEditar_alumne.menuAction())
        self.menubar.addAction(self.menuDocumentaci.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuSearchParticipant.setTitle(_translate("MainWindow", "Search Participant"))
        self.menuEditar_alumne.setTitle(_translate("MainWindow", "Editar alumne"))
        self.menuDocumentaci.setTitle(_translate("MainWindow", "Documentació"))
        self.actionDescarregar_Documentaci.setText(_translate("MainWindow", "Descarregar Documentació"))
        self.actionCanviar_correu.setText(_translate("MainWindow", "Canviar correu"))
