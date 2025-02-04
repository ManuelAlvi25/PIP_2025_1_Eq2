import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "metros_a_pies.ui"  #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.convertir)

    def convertir(self):
        try:
            metros=float(self.Metros.text())
            pies=metros * 3.28084

            # Muestra el resultado
            self.Resultado.setText(f"{metros:.2f} metros son {pies:.2f} pies.")
        except ValueError:
            # Si los valores ingresados no son válidos
            self.Resultado.setText("Ingresa un valor numérico válido.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
