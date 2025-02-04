import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E05_PESOS_A_DOLARES.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(10000000)
        self.horizontalSlider.setSingleStep(10)
        self.horizontalSlider.setValue(0) #Valor Inicial
        self.horizontalSlider.valueChanged.connect(self.CambiaValor)
        self.txt_valor.setText("0")
        self.txt_valor.textChanged.connect(self.dolares)



    # Area de los slots
    def CambiaValor(self):
        value = self.horizontalSlider.value()
        self.txt_valor.setText(str(value))
        self.dolares()


    def dolares(self):
        pesos = int(self.txt_valor.text())
        dolares = pesos * 0.049
        self.txt_valor_2.setText(str(dolares))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())