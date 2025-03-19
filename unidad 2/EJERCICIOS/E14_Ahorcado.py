import sys
import recursos_rc
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt


class JuegoAhorcado(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("E14_Ahorcado.ui", self)

        # Lista de palabras
        self.palabras = ["kazuya", "smash", "computadora", "ingenieria", "castores"]
        self.palabra_a_adivinar = None
        self.palabra_adivinada = None
        self.intentos_restantes = 6

        self.iniciar_juego()

        # Conectar el botón y el campo de texto
        self.pushButtonAdivinar.clicked.connect(self.adivinar_letra)
        self.lineEditLetra.textChanged.connect(self.verificar_entrada)
        self.dialIntentos.valueChanged.connect(self.cambiar_dificultad)

    def iniciar_juego(self):
        # Seleccionar una palabra aleatoria
        import random
        self.palabra_a_adivinar = random.choice(self.palabras)
        self.palabra_adivinada = ["_"] * len(self.palabra_a_adivinar)

        # Actualizar la interfaz
        self.labelPalabra.setText(" ".join(self.palabra_adivinada))
        self.labelIntentosRestantes.setText(f"Intentos Restantes: {self.intentos_restantes}")
        self.dialIntentos.setValue(self.intentos_restantes)
        self.labelResultado.setText("")
        self.lineEditLetra.clear()

    def cambiar_dificultad(self):
        # Cambiar la cantidad de intentos dependiendo del valor del dial
        dificultad = self.dialIntentos.value()

        if dificultad == 0:  # Fácil
            self.intentos_restantes = 10
            self.labelFácil.setStyleSheet("font-weight: bold; color: green;")
            self.labelMedio.setStyleSheet("font-weight: normal; color: black;")
            self.labelDifícil.setStyleSheet("font-weight: normal; color: black;")
        elif dificultad == 1:  # Medio
            self.intentos_restantes = 6
            self.labelFácil.setStyleSheet("font-weight: normal; color: black;")
            self.labelMedio.setStyleSheet("font-weight: bold; color: green;")
            self.labelDifícil.setStyleSheet("font-weight: normal; color: black;")
        else:  # Difícil
            self.intentos_restantes = 4
            self.labelFácil.setStyleSheet("font-weight: normal; color: black;")
            self.labelMedio.setStyleSheet("font-weight: normal; color: black;")
            self.labelDifícil.setStyleSheet("font-weight: bold; color: red;")

        # Reiniciar el juego con la nueva cantidad de intentos
        self.iniciar_juego()

    def adivinar_letra(self):
        letra = self.lineEditLetra.text().lower()
        if len(letra) == 1 and letra.isalpha():
            self.comprobar_adivinanza(letra)
        self.lineEditLetra.clear()

    def verificar_entrada(self):
        # Evitar la entrada de caracteres no alfabéticos
        texto = self.lineEditLetra.text()
        if texto and not texto.isalpha():
            self.lineEditLetra.setText("")

    def comprobar_adivinanza(self, letra):
        if letra in self.palabra_a_adivinar:
            for i in range(len(self.palabra_a_adivinar)):
                if self.palabra_a_adivinar[i] == letra:
                    self.palabra_adivinada[i] = letra
            self.labelPalabra.setText(" ".join(self.palabra_adivinada))
            if "_" not in self.palabra_adivinada:
                self.mostrar_resultado("¡Ganaste!")
        else:
            self.intentos_restantes -= 1
            self.labelIntentosRestantes.setText(f"Intentos Restantes: {self.intentos_restantes}")
            self.dialIntentos.setValue(self.intentos_restantes)
            if self.intentos_restantes == 0:
                self.mostrar_resultado("¡Juego Terminado!")

    def mostrar_resultado(self, mensaje):
        self.labelResultado.setText(mensaje)
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Fin del Juego")
        msg.setText(mensaje)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        self.iniciar_juego()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = JuegoAhorcado()
    ventana.show()
    sys.exit(app.exec_())
