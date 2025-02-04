import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile="E02_conversor_horas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnConvertir.clicked.connect(self.convertir_a_segundos)

    def convertir_a_segundos(self):
        hora_texto=self.lineEditHora.text().strip()

        if not hora_texto.isdigit():
            self.labelResultado.setText("Ingresa una hora válida (0-23).")
            return

        hora=int(hora_texto)
        if 0<=hora<=23:
            total_segundos=hora * 3600
            self.labelResultado.setText(f"Segundos: {total_segundos}")
        else:
            self.labelResultado.setText("La hora debe estar entre 0 y 23.")

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())
