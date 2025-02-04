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




    # Area de los slots
    def CambiaValor(self):
        value = self.SelectorImagen.value()
        self.txt_valor.setText(str(value))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())