import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P09_SliderImagenes_Manual.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.SelectorImagen.setMinimum(1)
        self.SelectorImagen.setMaximum(3)
        self.SelectorImagen.setSingleStep(1)
        self.SelectorImagen.setValue(1) #Valor Inicial
        self.SelectorImagen.valueChanged.connect(self.CambiaValor)


        self.diccionarioDatos = {
            1: (":/Ejercicios/nata.jpg",["Nata","22 años","corridos tumbados"]),
            2: (":/Ejercicios/kevin.jpg", ["kevin", "23 años", "folk"]),
            3: ("::/Ejercicios/ed maverick.jpg", ["ed", "23 años", "folk indie"])

        }
        self.indice = 1
        self.obtenerDatos()




    # Area de los slots
    def obtenerDatos(self):
        nombre = self.diccionarioDatos[self.indice][1][0]
        edad = self.diccionarioDatos[self.indice][1][1]
        musica = self.diccionarioDatos[self.indice][1][2]
        self.txt_nombre.setText(nombre)
        self.txt_edad.setText(edad)
        self.txt_musica.setText(musica)

        self.Imagen_Descripcion.setPixmap(QtGui.QPixmap(self.diccionarioDatos[self.indice][0]))


    def CambiaValor(self):
        self.indice = self.SelectorImagen.value()
        self.obtenerDatos()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())