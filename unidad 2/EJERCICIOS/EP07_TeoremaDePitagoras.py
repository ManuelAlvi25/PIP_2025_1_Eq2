import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "EP07_TeoremaDePitagoras.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.slider_cateto1.setMinimum(1)
        self.slider_cateto1.setMaximum(1000)
        self.slider_cateto1.setSingleStep(1)
        self.slider_cateto1.setValue(1)
        self.slider_cateto1.valueChanged.connect(self.actualizar_valores)

        self.slider_cateto2.setMinimum(1)
        self.slider_cateto2.setMaximum(1000)
        self.slider_cateto2.setSingleStep(1)
        self.slider_cateto2.setValue(1)
        self.slider_cateto2.valueChanged.connect(self.actualizar_valores)

        self.btn_calcular.clicked.connect(self.calcular_manual)

        self.txt_cateto1.setText("1")
        self.txt_cateto2.setText("1")
        self.txt_hipotenusa.setText(f"{(2**0.5):.3f}")

    def actualizar_valores(self):
        """ Obtiene los valores de los sliders y calcula la hipotenusa. """
        cateto1 = self.slider_cateto1.value()
        cateto2 = self.slider_cateto2.value()
        hipotenusa = (cateto1**2 + cateto2**2) ** 0.5
        self.txt_cateto1.setText(str(cateto1))
        self.txt_cateto2.setText(str(cateto2))
        self.txt_hipotenusa.setText(f"{hipotenusa:.3f}")

    def calcular_manual(self):
        """ Convierte los valores ingresados manualmente en los cuadros de texto. """
        try:
            cateto1 = int(self.txt_cateto1.text())
            cateto2 = int(self.txt_cateto2.text())

            if cateto1 <= 0 or cateto2 <= 0:
                self.txt_hipotenusa.setText("Valores > 0")
                return

            hipotenusa = (cateto1**2 + cateto2**2) ** 0.5
            self.txt_hipotenusa.setText(f"{hipotenusa:.3f}")

            self.slider_cateto1.setValue(cateto1)
            self.slider_cateto2.setValue(cateto2)
        except ValueError:
            self.txt_hipotenusa.setText("Error")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
