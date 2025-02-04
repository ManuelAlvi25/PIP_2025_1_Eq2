import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "P03_Ejemplo_ineEdit.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.btn_saludar.clicked.connect(self.saludar)

    # Area de los slots
    def saludar(self):
        cadena = self.txt_Nombre.text()
        if cadena != "":
            self.msj("Hola " + cadena + " buen dia! ")
        else:
             self.msj("debes poner nombre")


    def msj(self,txt):
      m= QtWidgets.QMessageBox()
      m.setText(txt)
      m.exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

