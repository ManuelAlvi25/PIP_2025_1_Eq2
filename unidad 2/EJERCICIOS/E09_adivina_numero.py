import sys
import random
from PyQt5 import uic, QtWidgets

qtCreatorFile="E09_adivina_numero.ui"
ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.numero_secreto=random.randint(1, 100)
        self.btnAdivinar.clicked.connect(self.verificar_numero)

    def verificar_numero(self):
        numero_texto=self.lineEditNumero.text()

        if not numero_texto.isdigit():
            self.labelResultado.setText("Ingresa un número válido")
            return

        numero_ingresado=int(numero_texto)
        if numero_ingresado<self.numero_secreto:
            self.labelResultado.setText("Muy bajo, intenta de nuevo")
        elif numero_ingresado>self.numero_secreto:
            self.labelResultado.setText("Muy alto, intenta de nuevo")
        else:
            self.labelResultado.setText("¡Correcto! Adivinaste el número")


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())

