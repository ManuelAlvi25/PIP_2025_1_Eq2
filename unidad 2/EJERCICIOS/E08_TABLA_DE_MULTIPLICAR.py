import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E08_TABLA_DE_MULTIPLICAR.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Configuración del slider
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)  # Valor inicial
        self.horizontalSlider.valueChanged.connect(self.actualizarValor)

        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(10)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.setValue(0)  # Valor inicial
        self.horizontalSlider_2.valueChanged.connect(self.actualizarValor2)

        # Configuración de los QLineEdit
        self.txt_v1.setText("0")
        self.txt_v2.setText("0")
        self.txt_v1.textChanged.connect(self.Multiplicar)
        self.txt_v2.textChanged.connect(self.Multiplicar)

    def actualizarValor(self):
        self.txt_v1.setText(str(self.horizontalSlider.value()))
        self.Multiplicar()

    def actualizarValor2(self):
        self.txt_v2.setText(str(self.horizontalSlider_2.value()))
        self.Multiplicar()

    def Multiplicar(self):
        try:
            valor1 = float(self.txt_v1.text())
            valor2 = float(self.txt_v2.text())
            r = valor1 * valor2
            self.txt_r.setText(str(r))
        except ValueError:
            self.txt_r.setText("Error")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
