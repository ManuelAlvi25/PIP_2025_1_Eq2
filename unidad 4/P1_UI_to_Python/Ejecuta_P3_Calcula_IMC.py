import sys
from PyQt5 import uic, QtWidgets

import P3_vPython_Calcula_IMC as interfaz

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #area de los signals

        self.btn_calcular.clicked.connect(self.calcular)

    #area de los slots
    def calcular(self):
        altura = float(self.txt_altura.text())
        peso = float(self.txt_peso.text())
        imc = peso/altura**2
        imc = round(imc,2)
        self.mensaje("El IMC es: " + str(imc))

    def mensaje(self, msj):
        n = QtWidgets.QMessageBox()
        n.setText(msj)
        n.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
