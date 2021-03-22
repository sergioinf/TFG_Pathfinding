from ventana_ui import *
from controlador import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.label.setText("Haz click en el botón para ejecutar A*")
        self.pushButton.setText("Púlsame")

        self.pushButton.clicked.connect(self.actualizar)

    def actualizar(self):
        self.label.setText("Ejecutando algoritmo, por favor espere")

        self.label.setText(calcular())



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
