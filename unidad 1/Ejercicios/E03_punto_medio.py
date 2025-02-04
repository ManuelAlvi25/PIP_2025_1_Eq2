import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile="punto_medio.ui"  # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calcular_punto_medio)

    def calcular_punto_medio(self):
        try:
            x1= float(self.X1.text())
            y1= float(self.Y1.text())
            x2= float(self.X2.text())
            y2= float(self.Y2.text())
            mx= (x1+x2)/2
            my= (y1+y2)/2

            self.Resultado.setText(f"Punto Medio: ({mx:.2f}, {my:.2f})")
        except ValueError:
            # Si los valores ingresados no son válidos
            self.Resultado.setText("Ingresa los valores numéricos válidos.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
