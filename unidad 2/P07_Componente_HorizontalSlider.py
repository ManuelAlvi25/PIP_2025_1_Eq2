import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P07_Componente_HorizontalSlider.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.horizontalSlider.setMinimum(-50)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setSingleStep(5)
        self.horizontalSlider.setValue(-50) #Valor Inicial
        self.horizontalSlider.valueChanged.connect(self.CambiaValor)
        self.txt_valor.setText("-50")


    # Area de los slots
    def CambiaValor(self):
        value = self.horizontalSlider.value()
        self.txt_valor.setText(str(value))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())