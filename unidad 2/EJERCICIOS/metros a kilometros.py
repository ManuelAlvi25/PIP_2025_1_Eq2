import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class Conversor(QMainWindow):
    def __init__(self):
        super(Conversor, self).__init__()
        loadUi("metros a kilometros.ui", self)
        self.pushButton_convertir.clicked.connect(self.convertir_distancia)
        self.dial.valueChanged.connect(self.actualizar_metros_con_dial)

    def convertir_distancia(self):
        try:
            metros = float(self.lineEdit_metros.text())
            kilometros = metros / 1000
            self.lineEdit_kilometros.setText(str(kilometros))
        except ValueError:
            self.lineEdit_kilometros.setText("Error: Ingresa un número")

    def actualizar_metros_con_dial(self):
        metros = self.dial.value()
        self.lineEdit_metros.setText(str(metros))
        self.convertir_distancia()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Conversor()
    window.show()
    sys.exit(app.exec_())