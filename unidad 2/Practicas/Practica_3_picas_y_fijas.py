import sys
import random
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "picas_y_fijas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btnCheck.clicked.connect(self.check_number)
        self.secret_number = self.generate_secret_number()
        self.attempts = []

    def generate_secret_number(self):
        digits = random.sample(range(10), 4)  # Genera 4 dígitos únicos
        return "".join(map(str, digits))

    def check_number(self):
        user_input = self.inputNumber.text()
        if len(user_input) != 4 or not user_input.isdigit() or len(set(user_input)) != 4:
            self.lblResult.setText("Ingresa un número válido de 4 dígitos únicos.")
            return

        picas, fijas = self.calculate_picas_fijas(user_input)
        result_text = f"Intento: {user_input} - Picas: {picas}, Fijas: {fijas}"
        self.attempts.append(result_text)
        self.history.setPlainText("\n".join(self.attempts))

        if fijas == 4:
            self.lblResult.setText("¡Felicidades! Adivinaste el número.")
        else:
            self.lblResult.setText(f"Picas: {picas}, Fijas: {fijas}")

    def calculate_picas_fijas(self, user_input):
        picas = sum(1 for i in range(4) if user_input[i] in self.secret_number and user_input[i] != self.secret_number[i])
        fijas = sum(1 for i in range(4) if user_input[i] == self.secret_number[i])
        return picas, fijas

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
