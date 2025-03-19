from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import QTimer
import sys

qtCreatorFile = "E17_Semaforo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.cambiar_luz)
        self.estado = 0  #0 = Rojo, 1 = Amarillo, 2 = Verde
        self.timer.start(2000)

    def cambiar_luz(self):
        if self.estado == 0:
            self.luz_roja.setStyleSheet("background-color: red;")
            self.luz_amarilla.setStyleSheet("background-color: gray;")
            self.luz_verde.setStyleSheet("background-color: gray;")
        elif self.estado == 1:
            self.luz_roja.setStyleSheet("background-color: gray;")
            self.luz_amarilla.setStyleSheet("background-color: yellow;")
            self.luz_verde.setStyleSheet("background-color: gray;")
        else:
            self.luz_roja.setStyleSheet("background-color: gray;")
            self.luz_amarilla.setStyleSheet("background-color: gray;")
            self.luz_verde.setStyleSheet("background-color: green;")

        self.estado = (self.estado + 1) % 3  # Cambia el estado


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())