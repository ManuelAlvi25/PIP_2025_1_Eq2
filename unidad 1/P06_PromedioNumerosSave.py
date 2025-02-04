import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "P06_PromedioNumerosSave.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_guardar.clicked.connect(self.guardar)
        self.calificaciones = []

    # Area de los slots

    def agregar(self):
        calificacion = int(self.txt_calificacion.text())
        self.calificaciones.append(calificacion)
        prom = sum(self.calificaciones)/len(self.calificaciones)
        self.txt_promedio.setText(str(prom))

    def guardar(self):
        archivo = open("Archivos/calificaciones.csv", "w")
        for c in self.calificaciones:
            archivo.write(str(c) + "\n")
        archivo.flush()
        archivo.close()

        self.msj("Archivo guardado con exito!")

    def msj(self,txt):
      m= QtWidgets.QMessageBox()
      m.setText(txt)
      m.exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

