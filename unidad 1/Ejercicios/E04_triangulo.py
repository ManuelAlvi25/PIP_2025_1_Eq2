import sys
from PyQt5 import uic, QtWidgets


qtCreatorFile = "triangulo.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calcular_area)

    def calcular_area(self):
        try:
            base = float(self.Base.text())
            altura = float(self.Altura.text())


            area = (base * altura) / 2


            self.Resultado.setText(f"El área del triángulo es: {area:.2f} unidades cuadradas.")
        except ValueError:

            self.Resultado.setText("Por favor, ingresa valores numéricos válidos.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

