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

        self.datosHPA.setText("Haz click en el botón para ejecutar JSP")
        self.ejecutaJSP.setText("Púlsame")

        self.ejecutaAEstrella.clicked.connect(self.actualizarAEstrella)
        self.ejecutaHPA.clicked.connect(self.actualizarHPA)
        self.ejecutaJSP.clicked.connect(self.actualizarJSP)

        self.ejecutaInseSG.clicked.connect(self.cInseSG)
        self.ejecutarCompAHPA.clicked.connect(self.cAHPA)
        self.ejecutarCompAJSP.clicked.connect(self.cJSP)



        j = open("mapasTratados\\mapasHPA32.txt", "rb")
        self.listaHPA=pickle.load(j)
        j.close()
        nombresHPA = [x.nombre for x in self.listaHPA]
        self.mapashpa.addItems(nombresHPA)
        self.mapascInseSG.addItems(nombresHPA)
        self.mapasCompAHPA.addItems(nombresHPA)

        j = open("mapasTratados\\mapasBase1.txt", "rb")
        self.listaA=pickle.load(j)
        j.close()
        nombresA = [k.nombre for k in self.listaA]
        self.mapasa.addItems(nombresA)
        self.mapasJSP.addItems(nombresA)
        self.mapasCompAJSP.addItems(nombresA)

    def actualizarJSP(self):
        self.datosJSP.setText("Ejecutando algoritmo, por favor espere")
        posMapa = self.mapasJSP.currentIndex()
        fI=self.filaIJSP.value()
        cI=self.columnaIJSP.value()
        fF=self.filaFJSP.value()
        cF=self.columnaFJSP.value()

        if self.listaA[posMapa].mapa[fI, cI]=='.' and self.listaA[posMapa].mapa[fF, cF]=='.':
            escribir = calcularJSP(self.listaA[posMapa], fI, cI, fF, cF, Agente(), False)

            if escribir == None:
                self.datosJSP.setText("Error, no se encuentra camino entre los puntos introducidos")
            else:
                self.datosJSP.setText(escribir[0])
                self.mapaJSP.setPixmap(QtGui.QPixmap(escribir[1]))
        elif self.listaA[posMapa].mapa[fI, cI]=='.':
            self.datosJSP.setText("Error, el punto de destino no esta en una posicion válida")
        else:
            self.datosJSP.setText("Error, el punto de origen no esta en una posicion válida")

    def actualizarAEstrella(self):
        self.datosAEstrella.setText("Ejecutando algoritmo, por favor espere")
        posMapa = self.mapasa.currentIndex()
        fI=self.filaIA.value()
        cI=self.columnaIA.value()
        fF=self.filaFA.value()
        cF=self.columnaFA.value()

        if self.listaA[posMapa].mapa[fI, cI]=='.' and self.listaA[posMapa].mapa[fF, cF]=='.':
            escribir = calcularA(self.listaA[posMapa], fI, cI, fF, cF, Agente(), False)

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
        self.datosHPA.setText("Ejecutando algoritmo, por favor espere")
        posMapa = self.mapashpa.currentIndex()
        fI=self.filaIHPA.value()
        cI=self.columnaIHPA.value()
        fF=self.filaFHPA.value()
        cF=self.columnaFHPA.value()

        if self.listaHPA[posMapa].mapa[fI, cI]=='.' and self.listaHPA[posMapa].mapa[fF, cF]=='.':
            self.datosHPA.setText("Ejecutando algoritmo")
            escribir = calcularHPA(self.listaHPA[posMapa], fI, cI, fF, cF, False)
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
        nPuntos = 100
        tiempo, exp = comparacionInsercion(posMapa, nPuntos)

        self.graficoTC.setPixmap(QtGui.QPixmap(tiempo))
        self.graficoNEC.setPixmap(QtGui.QPixmap(exp))

    def cAHPA(self):
        posMapa = self.mapascInseSG.currentIndex()
        nPuntos = 20
        tiempo, exp, err = comparacionAHPA(posMapa, nPuntos)
        self.graficoCompAHPAT.setPixmap(QtGui.QPixmap(tiempo))
        self.graficoCompAHPAN.setPixmap(QtGui.QPixmap(exp))
        self.graficoErrorHPA.setPixmap(QtGui.QPixmap(err))

    def cJSP(self):
        posMapa = self.mapasCompAJSP.currentIndex()
        nPuntos = 20
        tiempo, exp = comparacionAJSP(posMapa, nPuntos)
        self.graficoCompAJSPT.setPixmap(QtGui.QPixmap(tiempo))
        self.graficoCompAJSPN.setPixmap(QtGui.QPixmap(exp))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
