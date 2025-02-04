import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "imc.ui"  #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calcular_imc)

    def calcular_imc(self):
        try:
            #Obtener los valores de los campos de texto
            peso=float(self.Peso.text())
            altura=float(self.Altura.text())

            #Calcula el IMC
            imc=peso / (altura ** 2)

            #Determina la clasificación del IMC
            if imc<18.5:
                clasificacion="Bajo peso"
            elif imc<25:
                clasificacion="Peso normal"
            elif imc<30:
                clasificacion="Sobrepeso"
            else:
                clasificacion="Obesidad"

            # Mostrar el resultado
            resultado = f"Tu IMC es: {imc:.2f} ({clasificacion})"
            self.Resultado.setText(resultado)
        except ValueError:
            # Si los valores ingresados no son válidos
            self.Resultado.setText("Ingresa los valores.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
