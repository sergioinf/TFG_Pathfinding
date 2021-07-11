from ventana_ui import *
from controlador import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)


        self.setupUi(self)
        self.datosAEstrella.setText("Haz click en el botón para ejecutar A*")
        self.ejecutaAEstrella.setText("Púlsame")

        self.datosHPA.setText("Haz click en el botón para ejecutar HPA*")
        self.ejecutaHPA.setText("Púlsame")

        self.datosJPS.setText("Haz click en el botón para ejecutar JPS")
        self.ejecutaJPS.setText("Púlsame")

        self.ejecutaAEstrella.clicked.connect(self.actualizarAEstrella)
        self.ejecutaHPA.clicked.connect(self.actualizarHPA)
        self.ejecutaJPS.clicked.connect(self.actualizarJPS)

        self.ejecutaInseSG.clicked.connect(self.cInseSG)
        self.ejecutarCompAHPA.clicked.connect(self.cAHPA)
        self.ejecutarCompAJPS.clicked.connect(self.cJPS)
        self.ejecutarHPAJPS.clicked.connect(self.cHPAJPS)


        j = open("mapasTratados\\mapasHPA32.txt", "rb")
        self.listaHPA=pickle.load(j)
        j.close()
        nombresHPA = [x.nombre for x in self.listaHPA]
        self.mapashpa.addItems(nombresHPA)
        self.mapascInseSG.addItems(nombresHPA)
        self.mapasCompAHPA.addItems(nombresHPA)
        self.mapasHPAJPS.addItems(nombresHPA)

        j = open("mapasTratados\\mapasBase.txt", "rb")
        self.listaA=pickle.load(j)
        j.close()
        nombresA = [k.nombre for k in self.listaA]
        self.mapasa.addItems(nombresA)
        self.mapasJPS.addItems(nombresA)
        self.mapasCompAJPS.addItems(nombresA)

    def actualizarJPS(self):
        self.datosJPS.setText("Ejecutando algoritmo, por favor ePSere")
        posMapa = self.mapasJPS.currentIndex()
        fI=self.filaIJPS.value()
        cI=self.columnaIJPS.value()
        fF=self.filaFJPS.value()
        cF=self.columnaFJPS.value()


        if self.listaA[posMapa].matriz[fI, cI]=='.' and self.listaA[posMapa].matriz[fF, cF]=='.':
            escribir = calcularJPS(self.listaA[posMapa].copy(), fI, cI, fF, cF, False)
            if escribir == None:
                self.datosJPS.setText("Error, no se encuentra camino entre los puntos introducidos")
            else:
                self.datosJPS.setText(escribir[0])
                self.mapaJPS.setPixmap(QtGui.QPixmap(escribir[1]))
        elif self.listaA[posMapa].mapa[fI, cI]=='.':
            self.datosJPS.setText("Error, el punto de destino no esta en una posicion válida")
        else:
            self.datosJPS.setText("Error, el punto de origen no esta en una posicion válida")

    def actualizarAEstrella(self):
        self.datosAEstrella.setText("Ejecutando algoritmo, por favor ePSere")
        posMapa = self.mapasa.currentIndex()
        fI=self.filaIA.value()
        cI=self.columnaIA.value()
        fF=self.filaFA.value()
        cF=self.columnaFA.value()

        if self.listaA[posMapa].matriz[fI, cI]=='.' and self.listaA[posMapa].matriz[fF, cF]=='.':
            escribir = calcularA(self.listaA[posMapa].copy(), fI, cI, fF, cF, False)

            if escribir == None:
                self.datosAEstrella.setText("Error, no se encuentra camino entre los puntos introducidos")
            else:
                self.datosAEstrella.setText(escribir[0])
                self.mapaAEstrella.setPixmap(QtGui.QPixmap(escribir[1]))
        elif self.listaA[posMapa].mapa[fI, cI]=='.':
            self.datosA.setText("Error, el punto de destino no esta en una posicion válida")
        else:
            self.datosA.setText("Error, el punto de origen no esta en una posicion válida")

    def actualizarHPA(self):
        self.datosHPA.setText("Ejecutando algoritmo, por favor ePSere")
        posMapa = self.mapashpa.currentIndex()
        fI=self.filaIHPA.value()
        cI=self.columnaIHPA.value()
        fF=self.filaFHPA.value()
        cF=self.columnaFHPA.value()

        if self.listaHPA[posMapa].mapa[fI, cI]=='.' and self.listaHPA[posMapa].mapa[fF, cF]=='.':
            self.datosHPA.setText("Ejecutando algoritmo")
            print("voy a calcular HPA")
            escribir = calcularHPA(self.listaHPA[posMapa], fI, cI, fF, cF, False)
            print("Lo he calculado")
            if escribir == None:
                self.datosHPA.setText("Error, no existe camino entre los nodos introducidos")
            else:
                self.datosHPA.setText(escribir[0])
                self.mapaHPA.setPixmap(QtGui.QPixmap(escribir[1]))
        elif self.listaHPA[posMapa].mapa[fI, cI]=='.':
            self.datosHPA.setText("Error, el punto de destino no esta en una posicion válida")
        else:
            self.datosHPA.setText("Error, el punto de origen no esta en una posicion válida")

    def cInseSG(self):
        posMapa = self.mapascInseSG.currentIndex()
        nPuntos = self.nPuntosCINSE.value()
        sep = self.separacionCI.value()
        tiempo = comparacionInsercion(posMapa, nPuntos, sep)

        self.graficoTC.setPixmap(QtGui.QPixmap(tiempo))

    def cAHPA(self):
        posMapa = self.mapascInseSG.currentIndex()
        nPuntos = self.nPuntosAHPA.value()
        sep = self.separacionAHPA.value()
        tiempo, exp, err = comparacionAHPA(posMapa, nPuntos, sep)
        self.graficoCompAHPAT.setPixmap(QtGui.QPixmap(tiempo))
        self.graficoCompAHPAN.setPixmap(QtGui.QPixmap(exp))
        self.graficoErrorHPA.setPixmap(QtGui.QPixmap(err))

    def cJPS(self):
        posMapa = self.mapasCompAJPS.currentIndex()
        nPuntos = self.nPuntosAJPS.value()
        sep = self.separacionAJPS.value()
        tiempo, exp = comparacionAJPS(posMapa,nPuntos ,sep ,prueba=1)
        self.graficoCompAJPST.setPixmap(QtGui.QPixmap(tiempo))
        self.graficoCompAJPSN.setPixmap(QtGui.QPixmap(exp))

    def cHPAJPS(self):
        posMapa = self.mapasHPAJPS.currentIndex()
        print(posMapa)
        nPuntos = self.nPuntosHPAJPS.value()
        print(nPuntos)
        sep = self.separacionHPAJPS.value()
        print(sep)
        tiempo, exp = comparacionHPAJPS(posMapa, nPuntos, sep)
        self.graficoCompHPAJPST.setPixmap(QtGui.QPixmap(tiempo))
        self.graficoCompHPAJPSN.setPixmap(QtGui.QPixmap(exp))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
