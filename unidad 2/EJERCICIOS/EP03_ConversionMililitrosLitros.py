import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "EP03_ConversionMililitrosLitros.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(1000000)
        self.horizontalSlider.setSingleStep(5)
        self.horizontalSlider.setValue(0)
        self.horizontalSlider.valueChanged.connect(self.CambiaValor)

        # Configuración del botón de conversión
        self.btn_guardar.clicked.connect(self.ConvertirDesdeTexto)

        self.txt_valor.setText("0 ml")  # Valor inicial
        self.txt_litros.setText("0.000 L")  # Mostrar en litros

    def CambiaValor(self):
        """ Convierte el valor del slider y actualiza el cuadro de texto. """
        mililitros = self.horizontalSlider.value()
        litros = mililitros / 1000  # Conversión a litros
        self.txt_valor.setText(str(mililitros))  # Mostrar en ml
        self.txt_litros.setText(f"{litros:.3f} L")  # Mostrar en litros con 3 decimales

    def ConvertirDesdeTexto(self):
        """ Convierte el valor ingresado manualmente en el cuadro de texto. """
        try:
            mililitros = int(self.txt_valor.text())
            if mililitros < 0:
                self.txt_litros.setText("No negativos")
                return
            if mililitros > 1000000:
                self.txt_litros.setText("Maximo")
                return
            litros = mililitros / 1000
            self.txt_litros.setText(f"{litros:.3f} L")
            self.horizontalSlider.setValue(mililitros)
        except ValueError:
            self.txt_litros.setText("Error")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
