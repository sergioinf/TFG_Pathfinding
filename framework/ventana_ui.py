# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(938, 776)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.aEstrella = QtWidgets.QWidget()
        self.aEstrella.setObjectName("aEstrella")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.aEstrella)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayoutA = QtWidgets.QGridLayout()
        self.gridLayoutA.setObjectName("gridLayoutA")
        self.mapaAEstrella = QtWidgets.QLabel(self.aEstrella)
        self.mapaAEstrella.setText("")
        self.mapaAEstrella.setObjectName("mapaAEstrella")
        self.gridLayoutA.addWidget(self.mapaAEstrella, 0, 2, 9, 1)
        self.filaIAText = QtWidgets.QLabel(self.aEstrella)
        self.filaIAText.setObjectName("filaIAText")
        self.gridLayoutA.addWidget(self.filaIAText, 0, 0, 1, 1)
        self.filaIA = QtWidgets.QSpinBox(self.aEstrella)
        self.filaIA.setMaximum(511)
        self.filaIA.setObjectName("filaIA")
        self.gridLayoutA.addWidget(self.filaIA, 0, 1, 1, 1)
        self.columnaIA = QtWidgets.QSpinBox(self.aEstrella)
        self.columnaIA.setMaximum(511)
        self.columnaIA.setObjectName("columnaIA")
        self.gridLayoutA.addWidget(self.columnaIA, 1, 1, 1, 1)
        self.columnaIAText = QtWidgets.QLabel(self.aEstrella)
        self.columnaIAText.setObjectName("columnaIAText")
        self.gridLayoutA.addWidget(self.columnaIAText, 1, 0, 1, 1)
        self.filaFAText = QtWidgets.QLabel(self.aEstrella)
        self.filaFAText.setObjectName("filaFAText")
        self.gridLayoutA.addWidget(self.filaFAText, 2, 0, 1, 1)
        self.filaFA = QtWidgets.QSpinBox(self.aEstrella)
        self.filaFA.setMaximum(511)
        self.filaFA.setObjectName("filaFA")
        self.gridLayoutA.addWidget(self.filaFA, 2, 1, 1, 1)
        self.columnaFA = QtWidgets.QSpinBox(self.aEstrella)
        self.columnaFA.setMaximum(511)
        self.columnaFA.setObjectName("columnaFA")
        self.gridLayoutA.addWidget(self.columnaFA, 3, 1, 1, 1)
        self.columnaFAText = QtWidgets.QLabel(self.aEstrella)
        self.columnaFAText.setObjectName("columnaFAText")
        self.gridLayoutA.addWidget(self.columnaFAText, 3, 0, 1, 1)
        self.mapaaText = QtWidgets.QLabel(self.aEstrella)
        self.mapaaText.setObjectName("mapaaText")
        self.gridLayoutA.addWidget(self.mapaaText, 4, 0, 1, 1)
        self.mapasa = QtWidgets.QComboBox(self.aEstrella)
        self.mapasa.setObjectName("mapasa")
        self.gridLayoutA.addWidget(self.mapasa, 4, 1, 1, 1)
        self.datosAEstrella = QtWidgets.QLabel(self.aEstrella)
        self.datosAEstrella.setObjectName("datosAEstrella")
        self.gridLayoutA.addWidget(self.datosAEstrella, 5, 0, 3, 2)
        self.ejecutaAEstrella = QtWidgets.QPushButton(self.aEstrella)
        self.ejecutaAEstrella.setObjectName("ejecutaAEstrella")
        self.gridLayoutA.addWidget(self.ejecutaAEstrella, 8, 0, 1, 2)
        self.horizontalLayout_3.addLayout(self.gridLayoutA)
        self.tabWidget.addTab(self.aEstrella, "")
        self.hpaEstrella = QtWidgets.QWidget()
        self.hpaEstrella.setObjectName("hpaEstrella")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.hpaEstrella)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayoutHPA = QtWidgets.QGridLayout()
        self.gridLayoutHPA.setObjectName("gridLayoutHPA")
        self.mapashpa = QtWidgets.QComboBox(self.hpaEstrella)
        self.mapashpa.setObjectName("mapashpa")
        self.gridLayoutHPA.addWidget(self.mapashpa, 4, 1, 1, 1)
        self.mapahpaText = QtWidgets.QLabel(self.hpaEstrella)
        self.mapahpaText.setObjectName("mapahpaText")
        self.gridLayoutHPA.addWidget(self.mapahpaText, 4, 0, 1, 1)
        self.mapaHPA = QtWidgets.QLabel(self.hpaEstrella)
        self.mapaHPA.setText("")
        self.mapaHPA.setObjectName("mapaHPA")
        self.gridLayoutHPA.addWidget(self.mapaHPA, 0, 2, 8, 1)
        self.columnaIhpaText = QtWidgets.QLabel(self.hpaEstrella)
        self.columnaIhpaText.setObjectName("columnaIhpaText")
        self.gridLayoutHPA.addWidget(self.columnaIhpaText, 1, 0, 1, 1)
        self.filaIhpaText = QtWidgets.QLabel(self.hpaEstrella)
        self.filaIhpaText.setObjectName("filaIhpaText")
        self.gridLayoutHPA.addWidget(self.filaIhpaText, 0, 0, 1, 1)
        self.filaFHPAText = QtWidgets.QLabel(self.hpaEstrella)
        self.filaFHPAText.setObjectName("filaFHPAText")
        self.gridLayoutHPA.addWidget(self.filaFHPAText, 2, 0, 1, 1)
        self.datosHPA = QtWidgets.QLabel(self.hpaEstrella)
        self.datosHPA.setObjectName("datosHPA")
        self.gridLayoutHPA.addWidget(self.datosHPA, 5, 0, 2, 2)
        self.filaIHPA = QtWidgets.QSpinBox(self.hpaEstrella)
        self.filaIHPA.setMaximum(511)
        self.filaIHPA.setObjectName("filaIHPA")
        self.gridLayoutHPA.addWidget(self.filaIHPA, 0, 1, 1, 1)
        self.ejecutaHPA = QtWidgets.QPushButton(self.hpaEstrella)
        self.ejecutaHPA.setObjectName("ejecutaHPA")
        self.gridLayoutHPA.addWidget(self.ejecutaHPA, 7, 0, 1, 2)
        self.columnaIHPA = QtWidgets.QSpinBox(self.hpaEstrella)
        self.columnaIHPA.setMaximum(511)
        self.columnaIHPA.setObjectName("columnaIHPA")
        self.gridLayoutHPA.addWidget(self.columnaIHPA, 1, 1, 1, 1)
        self.columnaFHPAText = QtWidgets.QLabel(self.hpaEstrella)
        self.columnaFHPAText.setObjectName("columnaFHPAText")
        self.gridLayoutHPA.addWidget(self.columnaFHPAText, 3, 0, 1, 1)
        self.filaFHPA = QtWidgets.QSpinBox(self.hpaEstrella)
        self.filaFHPA.setMaximum(511)
        self.filaFHPA.setObjectName("filaFHPA")
        self.gridLayoutHPA.addWidget(self.filaFHPA, 2, 1, 1, 1)
        self.columnaFHPA = QtWidgets.QSpinBox(self.hpaEstrella)
        self.columnaFHPA.setMaximum(511)
        self.columnaFHPA.setObjectName("columnaFHPA")
        self.gridLayoutHPA.addWidget(self.columnaFHPA, 3, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayoutHPA)
        self.tabWidget.addTab(self.hpaEstrella, "")
        self.JSP = QtWidgets.QWidget()
        self.JSP.setObjectName("JSP")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.JSP)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayoutJSP = QtWidgets.QGridLayout()
        self.gridLayoutJSP.setObjectName("gridLayoutJSP")
        self.mapaJSPText = QtWidgets.QLabel(self.JSP)
        self.mapaJSPText.setObjectName("mapaJSPText")
        self.gridLayoutJSP.addWidget(self.mapaJSPText, 4, 0, 1, 1)
        self.columnaFJSPText = QtWidgets.QLabel(self.JSP)
        self.columnaFJSPText.setObjectName("columnaFJSPText")
        self.gridLayoutJSP.addWidget(self.columnaFJSPText, 3, 0, 1, 1)
        self.filaFJSPText = QtWidgets.QLabel(self.JSP)
        self.filaFJSPText.setObjectName("filaFJSPText")
        self.gridLayoutJSP.addWidget(self.filaFJSPText, 2, 0, 1, 1)
        self.columnaIJSPText = QtWidgets.QLabel(self.JSP)
        self.columnaIJSPText.setObjectName("columnaIJSPText")
        self.gridLayoutJSP.addWidget(self.columnaIJSPText, 1, 0, 1, 1)
        self.filaIJSPText = QtWidgets.QLabel(self.JSP)
        self.filaIJSPText.setObjectName("filaIJSPText")
        self.gridLayoutJSP.addWidget(self.filaIJSPText, 0, 0, 1, 1)
        self.columnaIJSP = QtWidgets.QSpinBox(self.JSP)
        self.columnaIJSP.setMaximum(511)
        self.columnaIJSP.setObjectName("columnaIJSP")
        self.gridLayoutJSP.addWidget(self.columnaIJSP, 1, 1, 1, 1)
        self.filaFJSP = QtWidgets.QSpinBox(self.JSP)
        self.filaFJSP.setMaximum(511)
        self.filaFJSP.setObjectName("filaFJSP")
        self.gridLayoutJSP.addWidget(self.filaFJSP, 2, 1, 1, 1)
        self.columnaFJSP = QtWidgets.QSpinBox(self.JSP)
        self.columnaFJSP.setMaximum(511)
        self.columnaFJSP.setObjectName("columnaFJSP")
        self.gridLayoutJSP.addWidget(self.columnaFJSP, 3, 1, 1, 1)
        self.mapasJSP = QtWidgets.QComboBox(self.JSP)
        self.mapasJSP.setObjectName("mapasJSP")
        self.gridLayoutJSP.addWidget(self.mapasJSP, 4, 1, 1, 1)
        self.filaIJSP = QtWidgets.QSpinBox(self.JSP)
        self.filaIJSP.setMaximum(511)
        self.filaIJSP.setObjectName("filaIJSP")
        self.gridLayoutJSP.addWidget(self.filaIJSP, 0, 1, 1, 1)
        self.datosJSP = QtWidgets.QLabel(self.JSP)
        self.datosJSP.setObjectName("datosJSP")
        self.gridLayoutJSP.addWidget(self.datosJSP, 5, 0, 2, 2)
        self.ejecutaJSP = QtWidgets.QPushButton(self.JSP)
        self.ejecutaJSP.setObjectName("ejecutaJSP")
        self.gridLayoutJSP.addWidget(self.ejecutaJSP, 7, 0, 1, 2)
        self.mapaJSP = QtWidgets.QLabel(self.JSP)
        self.mapaJSP.setText("")
        self.mapaJSP.setObjectName("mapaJSP")
        self.gridLayoutJSP.addWidget(self.mapaJSP, 0, 4, 8, 1)
        self.horizontalLayout_4.addLayout(self.gridLayoutJSP)
        self.tabWidget.addTab(self.JSP, "")
        self.comparacion = QtWidgets.QWidget()
        self.comparacion.setObjectName("comparacion")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.comparacion)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.comparacion)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 894, 671))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.mapascInseSG = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.mapascInseSG.setObjectName("mapascInseSG")
        self.gridLayout.addWidget(self.mapascInseSG, 3, 1, 1, 1)
        self.ejecutaInseSG = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ejecutaInseSG.setObjectName("ejecutaInseSG")
        self.gridLayout.addWidget(self.ejecutaInseSG, 3, 2, 1, 1)
        self.mapacInseSGText = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.mapacInseSGText.setObjectName("mapacInseSGText")
        self.gridLayout.addWidget(self.mapacInseSGText, 3, 0, 1, 1)
        self.cInseSGText = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.cInseSGText.setFont(font)
        self.cInseSGText.setObjectName("cInseSGText")
        self.gridLayout.addWidget(self.cInseSGText, 0, 0, 2, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        self.graficoTC = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.graficoTC.setText("")
        self.graficoTC.setObjectName("graficoTC")
        self.verticalLayout.addWidget(self.graficoTC)
        self.graficoNEC = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.graficoNEC.setText("")
        self.graficoNEC.setObjectName("graficoNEC")
        self.verticalLayout.addWidget(self.graficoNEC)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mapasCompAHPA = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.mapasCompAHPA.setObjectName("mapasCompAHPA")
        self.gridLayout_3.addWidget(self.mapasCompAHPA, 1, 1, 1, 1)
        self.mapaCompAHPAText = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.mapaCompAHPAText.setObjectName("mapaCompAHPAText")
        self.gridLayout_3.addWidget(self.mapaCompAHPAText, 1, 0, 1, 1)
        self.ejecutarCompAHPA = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ejecutarCompAHPA.setObjectName("ejecutarCompAHPA")
        self.gridLayout_3.addWidget(self.ejecutarCompAHPA, 1, 2, 1, 1)
        self.cAHPAText = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.cAHPAText.setFont(font)
        self.cAHPAText.setObjectName("cAHPAText")
        self.gridLayout_3.addWidget(self.cAHPAText, 0, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.graficoCompAHPAT = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.graficoCompAHPAT.setText("")
        self.graficoCompAHPAT.setObjectName("graficoCompAHPAT")
        self.verticalLayout.addWidget(self.graficoCompAHPAT)
        self.graficoCompAHPAN = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.graficoCompAHPAN.setText("")
        self.graficoCompAHPAN.setObjectName("graficoCompAHPAN")
        self.verticalLayout.addWidget(self.graficoCompAHPAN)
        self.graficoErrorHPA = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.graficoErrorHPA.setText("")
        self.graficoErrorHPA.setObjectName("graficoErrorHPA")
        self.verticalLayout.addWidget(self.graficoErrorHPA)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mapasCompAJSP = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.mapasCompAJSP.setObjectName("mapasCompAJSP")
        self.gridLayout_2.addWidget(self.mapasCompAJSP, 1, 1, 1, 1)
        self.mapasCompAJSPText = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.mapasCompAJSPText.setObjectName("mapasCompAJSPText")
        self.gridLayout_2.addWidget(self.mapasCompAJSPText, 1, 0, 1, 1)
        self.ejecutarCompAJSP = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ejecutarCompAJSP.setObjectName("ejecutarCompAJSP")
        self.gridLayout_2.addWidget(self.ejecutarCompAJSP, 1, 2, 1, 1)
        self.cAJSPText = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.cAJSPText.setFont(font)
        self.cAJSPText.setObjectName("cAJSPText")
        self.gridLayout_2.addWidget(self.cAJSPText, 0, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.graficoCompAJSPN = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.graficoCompAJSPN.setText("")
        self.graficoCompAJSPN.setObjectName("graficoCompAJSPN")
        self.verticalLayout.addWidget(self.graficoCompAJSPN)
        self.graficoCompAJSPT = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.graficoCompAJSPT.setText("")
        self.graficoCompAJSPT.setObjectName("graficoCompAJSPT")
        self.verticalLayout.addWidget(self.graficoCompAJSPT)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.comparacion, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 938, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filaIAText.setText(_translate("MainWindow", "Fila inicial"))
        self.columnaIAText.setText(_translate("MainWindow", "Columna inicial"))
        self.filaFAText.setText(_translate("MainWindow", "Fila final"))
        self.columnaFAText.setText(_translate("MainWindow", "Columna final"))
        self.mapaaText.setText(_translate("MainWindow", "Mapa"))
        self.datosAEstrella.setText(_translate("MainWindow", "Ejecuta el programa para A*"))
        self.ejecutaAEstrella.setText(_translate("MainWindow", "Ejecutar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aEstrella), _translate("MainWindow", "A*"))
        self.mapahpaText.setText(_translate("MainWindow", "Mapa"))
        self.columnaIhpaText.setText(_translate("MainWindow", "Columna inicial"))
        self.filaIhpaText.setText(_translate("MainWindow", "Fila inicial"))
        self.filaFHPAText.setText(_translate("MainWindow", "Fila final"))
        self.datosHPA.setText(_translate("MainWindow", "Ejecuta el programa para HPA*"))
        self.ejecutaHPA.setText(_translate("MainWindow", "Ejecutar"))
        self.columnaFHPAText.setText(_translate("MainWindow", "Columna final"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hpaEstrella), _translate("MainWindow", "HPA*"))
        self.mapaJSPText.setText(_translate("MainWindow", "Mapa"))
        self.columnaFJSPText.setText(_translate("MainWindow", "Columna final"))
        self.filaFJSPText.setText(_translate("MainWindow", "Fila final"))
        self.columnaIJSPText.setText(_translate("MainWindow", "Columna inicial"))
        self.filaIJSPText.setText(_translate("MainWindow", "Fila inicial"))
        self.datosJSP.setText(_translate("MainWindow", "Ejecuta el programa para JSP"))
        self.ejecutaJSP.setText(_translate("MainWindow", "Ejecutar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.JSP), _translate("MainWindow", "JSP"))
        self.ejecutaInseSG.setText(_translate("MainWindow", "Ejecutar"))
        self.mapacInseSGText.setText(_translate("MainWindow", "Mapa"))
        self.cInseSGText.setText(_translate("MainWindow", "Costes de inserción de los puntos de salida y destino en los grafos para HPA*"))
        self.mapaCompAHPAText.setText(_translate("MainWindow", "Mapa"))
        self.ejecutarCompAHPA.setText(_translate("MainWindow", "Ejecutar"))
        self.cAHPAText.setText(_translate("MainWindow", "Comparación entre A* y HPA*"))
        self.mapasCompAJSPText.setText(_translate("MainWindow", "Mapa"))
        self.ejecutarCompAJSP.setText(_translate("MainWindow", "Ejecutar"))
        self.cAJSPText.setText(_translate("MainWindow", "Comparacion entre A* y JSP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.comparacion), _translate("MainWindow", "Comparaciones"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
