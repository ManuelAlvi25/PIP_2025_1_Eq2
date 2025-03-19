from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer
import sys
import os

qtCreatorFile = "E18_OpcionImagen.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Lista de preguntas con imagen y respuestas
        self.preguntas = [
            {"imagen": r"C:\Users\Manuel\Desktop\PIP_2025_1_Eq0\archivos\kevin.jpg", "opciones": ["Kevin Kaarl", "Ed maverick", "Bryan Kaarl"], "correcta": "Kevin Kaarl"},
            {"imagen": r"C:\Users\Manuel\Desktop\PIP_2025_1_Eq0\archivos\geto.jpg", "opciones": ["Gojo", "Goku", "Geto"], "correcta": "Geto"},
            {"imagen": r"C:\Users\Manuel\Desktop\PIP_2025_1_Eq0\archivos\miles.jpg", "opciones": ["Peter Parker", "Miles morales", "Matt murdock"], "correcta": "Miles morales"}
        ]

        self.indice_pregunta = 0  # Índice de la pregunta actual
        self.puntaje = 0  # Contador de respuestas correctas

        # Conectar botones a la función de verificación
        self.btn_opcion1.clicked.connect(self.verificar_respuesta)
        self.btn_opcion2.clicked.connect(self.verificar_respuesta)
        self.btn_opcion3.clicked.connect(self.verificar_respuesta)

        # Cargar la primera pregunta
        self.cargar_pregunta()

    def cargar_pregunta(self):
        """Carga la pregunta actual en la interfaz."""
        if self.indice_pregunta < len(self.preguntas):
            pregunta = self.preguntas[self.indice_pregunta]

            # Cargar la imagen usando QPixmap
            if os.path.exists(pregunta['imagen']):
                pixmap = QtGui.QPixmap(pregunta['imagen'])
                pixmap = pixmap.scaled(self.lbl_imagen.size(), QtCore.Qt.KeepAspectRatio)
                self.lbl_imagen.setPixmap(pixmap)
            else:
                print(f"El archivo {pregunta['imagen']} no existe.")

            # Asignar texto a los botones
            self.btn_opcion1.setText(pregunta["opciones"][0])
            self.btn_opcion2.setText(pregunta["opciones"][1])
            self.btn_opcion3.setText(pregunta["opciones"][2])

            # Borrar mensaje anterior
            self.lbl_resultado.setText("")
        else:
            # Si no hay más preguntas, mostrar el puntaje final
            self.lbl_imagen.clear()  # Quitar imagen
            self.btn_opcion1.hide()
            self.btn_opcion2.hide()
            self.btn_opcion3.hide()
            self.lbl_resultado.setText(f"Juego terminado. Puntaje: {self.puntaje}/{len(self.preguntas)}")

    def verificar_respuesta(self):
        """Verifica si la respuesta seleccionada es correcta."""
        pregunta = self.preguntas[self.indice_pregunta]
        respuesta = self.sender().text()  # Obtener el texto del botón presionado

        if respuesta == pregunta["correcta"]:
            self.puntaje += 1
            self.lbl_resultado.setText("✅ Correcto!")
        else:
            self.lbl_resultado.setText(f"❌ Incorrecto! Era: {pregunta['correcta']}")

        # Pasar a la siguiente pregunta después de 1 segundo
        self.indice_pregunta += 1
        QTimer.singleShot(1000, self.cargar_pregunta)  # Espera 1 segundo antes de cambiar


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())