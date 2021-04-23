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

        self.ejecutaAEstrella.clicked.connect(self.actualizarAEstrella)
        self.ejecutaHPA.clicked.connect(self.actualizarHPA)

    def actualizarAEstrella(self):
        self.datosAEstrella.setText("Ejecutando algoritmo, por favor espere")
        escribir = calcularA()
        self.datosAEstrella.setText(escribir[0])
        self.mapaAEstrella.setPixmap(QtGui.QPixmap(escribir[1]))

    def actualizarHPA(self):
        self.datosHPA.setText("Ejecutando algoritmo, por favor espere")
        escribir = calcularHPA()
        self.datosHPA.setText(escribir[0])
        self.mapaHPA.setPixmap(QtGui.QPixmap(escribir[1]))



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
