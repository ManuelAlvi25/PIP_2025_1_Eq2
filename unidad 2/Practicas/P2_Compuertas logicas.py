import sys
import recursos_rc
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()

        loadUi("P2_Compuertas logicas.ui", self)
        self.andButton.clicked.connect(self.handleAndGate)
        self.orButton.clicked.connect(self.handleOrGate)
        self.notButton.clicked.connect(self.handleNotGate)
        self.xorButton.clicked.connect(self.handleXorGate)


    def handleAndGate(self):

        a = self.inputA.isChecked()
        b = self.inputB.isChecked()

        result = a and b

        self.outputLabel.setText(str(int(result)))

    def handleOrGate(self):
        a = self.inputA.isChecked()
        b = self.inputB.isChecked()

        result = a or b

        self.outputLabel.setText(str(int(result)))

    def handleNotGate(self):
        a = self.inputA.isChecked()

        result = not a

        self.outputLabel.setText(str(int(result)))

    def handleXorGate(self):

        a = self.inputA.isChecked()
        b = self.inputB.isChecked()

        result = a ^ b

        self.outputLabel.setText(str(int(result)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())  
