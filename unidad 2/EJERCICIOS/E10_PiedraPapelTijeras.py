import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import recursos_rc

class PiedraPapelTijeras(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("E10_PiedraPapelTijeras.ui", self)

        # Diccionario de imágenes con rutas desde el archivo de recursos
        self.imagenes = {
            "Piedra": r"C:\Users\Manuel\Desktop\PIP_2025_1_Eq0\archivos\Piedra.jpg",
            "Papel": r":C:\Users\Manuel\Desktop\PIP_2025_1_Eq0\archivos\Papel.jpg",
            "Tijeras": r"C:\Users\Manuel\Desktop\PIP_2025_1_Eq0\archivos\Tijeras.jpg"
        }
        # Conectar botones con funciones
        self.btn_Piedra.clicked.connect(lambda: self.jugar("Piedra"))
        self.btn_Papel.clicked.connect(lambda: self.jugar("Papel"))
        self.btn_Tijeras.clicked.connect(lambda: self.jugar("Tijeras"))

    def jugar(self, eleccion_usuario):
        # Mostrar elección del usuario
        self.Eleccion_Usuario.setPixmap(QPixmap(self.imagenes[eleccion_usuario]))

        # Elección aleatoria de la computadora
        eleccion_computadora = random.choice(["Piedra", "Papel", "Tijeras"])
        self.Eleccion_Computadora.setPixmap(QPixmap(self.imagenes[eleccion_computadora]))

        # Determinar el resultado
        resultado = self.determinar_ganador(eleccion_usuario, eleccion_computadora)
        self.txt_Resultado.setText(resultado)

    def determinar_ganador(self, usuario, computadora):
        if usuario == computadora:
            return "¡Empate!"
        elif (usuario == "Piedra" and computadora == "Tijeras") or \
                (usuario == "Papel" and computadora == "Piedra") or \
                (usuario == "Tijeras" and computadora == "Papel"):
            return "¡Ganaste!"
        else:
            return "¡Perdiste!"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PiedraPapelTijeras()
    ventana.show()
    sys.exit(app.exec_())
