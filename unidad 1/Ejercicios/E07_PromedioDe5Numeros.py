import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "E07_PromedioDe5Numeros.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.PROMEDIO.clicked.connect(self.Cpromedio)

        # Area de los slots
    def Cpromedio(self):
        try:
            a = float(self.A.text())
            b = float(self.B.text())
            c = float(self.C.text())
            d = float(self.D.text())
            e = float(self.E.text())
            suma = a + b + c + d + e
            Promedio = suma // 5
            self.msj("El promedio es " + str(Promedio))
        except Exception as error:
            print(error)


    def msj(self,txt):
      m= QtWidgets.QMessageBox()
      m.setText(txt)
      m.exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

