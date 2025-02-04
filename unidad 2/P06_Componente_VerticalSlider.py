import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P05_Componente_VerticalSlider.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.verticalSlider.setMinimum(-50)
        self.verticalSlider.setMaximum(50)
        self.verticalSlider.setSingleStep(5)
        self.verticalSlider.setValue(-50) #Valor Inicial
        self.verticalSlider.valueChanged.connect(self.CambiaValor)
        self.txt_valor.setText("-50")


    # Area de los slots
    def CambiaValor(self):
        value = self.verticalSlider.value()
        self.txt_valor.setText(str(value))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())