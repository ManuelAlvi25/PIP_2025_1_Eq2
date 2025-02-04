import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class Conversor(QMainWindow):
    def __init__(self):
        super(Conversor, self).__init__()
        loadUi("Cambio de grados centigrados fahrenheit.ui", self)
        self.pushButton_convertir.clicked.connect(self.convertir_temperatura)
        self.horizontalSlider.valueChanged.connect(self.actualizar_celsius_con_slider)

    def convertir_temperatura(self):
        try:
            celsius = float(self.lineEdit_celsius.text())
            fahrenheit = (celsius * 9/5) + 32
            self.lineEdit_fahrenheit.setText(str(fahrenheit))
        except ValueError:
            self.lineEdit_fahrenheit.setText("Error: Ingresa un número")

    def actualizar_celsius_con_slider(self):
        celsius = self.horizontalSlider.value()
        self.lineEdit_celsius.setText(str(celsius))
        self.convertir_temperatura()  # Actualiza Fahrenheit automáticamente

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Conversor()
    window.show()
    sys.exit(app.exec_())