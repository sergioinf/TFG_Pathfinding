from ventana_ui import *
from controlador import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)


        self.setupUi(self)
        self.label.setText("Haz click en el botón para ejecutar A*")
        self.pushButton.setText("Púlsame")


        self.pushButton.clicked.connect(self.actualizar)

    def actualizar(self):
        self.label.setText("Ejecutando algoritmo, por favor espere")
        escribir = calcular()
        self.label.setText(escribir[0])
        self.imagen.setPixmap(QtGui.QPixmap(escribir[1]))



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
