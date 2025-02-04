import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E06_AREA_PENTAGONO.ui"
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
        self.horizontalSlider.valueChanged.connect(self.actualizarPerimetro)

        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(1000)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.setValue(0)  # Valor inicial
        self.horizontalSlider_2.valueChanged.connect(self.actualizarApotema)

        # Configuración de los QLineEdit
        self.txt_perimetro.setText("0")
        self.txt_apotema.setText("0")
        self.txt_perimetro.textChanged.connect(self.calcularArea)
        self.txt_apotema.textChanged.connect(self.calcularArea)

    def actualizarPerimetro(self):
        self.txt_perimetro.setText(str(self.horizontalSlider.value()))
        self.calcularArea()

    def actualizarApotema(self):
        self.txt_apotema.setText(str(self.horizontalSlider_2.value()))
        self.calcularArea()

    def calcularArea(self):
        try:
            perimetro = float(self.txt_perimetro.text())
            apotema = float(self.txt_apotema.text())
            area = (perimetro * apotema) / 2
            self.txt_area.setText(str(area))
        except ValueError:
            self.txt_area.setText("Error")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
