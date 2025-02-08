import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P08_DescripcionDeImagenes.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.SelectorImagen.setMinimum(1)
        self.SelectorImagen.setMaximum(1)
        self.SelectorImagen.setSingleStep(1)
        self.SelectorImagen.setValue(1) #Valor Inicial
        self.SelectorImagen.valueChanged.connect(self.CambiaValor)


        self.diccionarioDatos = {
            0: (":/Ejercicios/nata.jpg",["Nata","22 años","corridos tumbados"]),
            1: (":/Ejercicios/kevin.jpg", ["kevin", "22 años", "folk"]),
            2: ("::/Ejercicios/ed maverick.jpg", ["ed", "22 años", "folk"])

        }
        self.indice = 0
        self.obtenerDatos()




    # Area de los slots
    def obtenerDatos(self):
        nombre = self.diccionarioDatos[self.indice][1][0]
        edad = self.diccionarioDatos[self.indice][1][1]
        musica = self.diccionarioDatos[self.indice][1][2]
        self.txt_nombre.setText(nombre)
        self.txt_edad.setText(edad)
        self.txt_musica.setText(musica)


    def CambiaValor(self):
        value = self.SelectorImagen.value()
        self.txt_valor.setText(str(value))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())