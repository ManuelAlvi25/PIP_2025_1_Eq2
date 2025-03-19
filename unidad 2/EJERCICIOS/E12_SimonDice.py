import sys
import random
import time
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.uic.properties import QtCore

qtCreatorFile = "E12_SimonDice.ui"  # Archivo de Qt Designer
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MemoryGame(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar botones a funciones
        self.btnStart.clicked.connect(self.generate_pattern)
        self.btnCheck.clicked.connect(self.check_pattern)

        # Lista de botones del juego
        self.buttons = [self.btn1, self.btn2, self.btn3, self.btn4]

        for btn in self.buttons:
            btn.clicked.connect(self.record_user_input)

        # Cargar imagen en QLabel
        self.lblImage.setPixmap(QPixmap(r"C:\Users\Manuel\Desktop\PIP_2025_1_Eq0\archivos\simondice.jpg"))
        self.lblImage.setScaledContents(True)

        # Variables del juego
        self.pattern = []
        self.user_pattern = []
        self.current_step = 0

        # Temporizador para mostrar la secuencia
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_next_step)

    def generate_pattern(self):
        """Genera una secuencia aleatoria y la muestra."""
        self.pattern = random.sample(range(len(self.buttons)), len(self.buttons))
        self.user_pattern = []
        self.lblResult.setText("Memoriza el patrón y repítelo.")

        # Reiniciar colores de los botones
        for btn in self.buttons:
            btn.setStyleSheet("")

        self.current_step = 0
        self.timer.start(1000)  # Inicia el temporizador (1 seg por botón)

    def show_next_step(self):
        """Muestra cada paso de la secuencia iluminando los botones."""
        if self.current_step < len(self.pattern):
            index = self.pattern[self.current_step]
            button = self.buttons[index]

            button.setStyleSheet("background-color: yellow;")

            # Nuevo temporizador para apagar el botón después de 500ms
            QtCore.QTimer.singleShot(500, lambda: button.setStyleSheet(""))

            self.current_step += 1
        else:
            self.timer.stop()  # Detiene la animación cuando termina

    def record_user_input(self):
        """Registra la secuencia que el usuario ingresa."""
        sender = self.sender()
        index = self.buttons.index(sender)
        self.user_pattern.append(index)

    def check_pattern(self):
        """Verifica si la secuencia del usuario es correcta."""
        if self.user_pattern == self.pattern:
            self.lblResult.setText("¡Correcto!")
        else:
            self.lblResult.setText("Incorrecto, intenta de nuevo.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MemoryGame()
    window.show()
    sys.exit(app.exec())
