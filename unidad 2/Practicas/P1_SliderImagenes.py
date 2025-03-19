import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

# Cargar el archivo UI usando uic.loadUiType
qtCreatorFile = "P1_SliderImagenes.ui"  # Asegúrate de que el nombre del archivo coincida
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MainWindow(QtBaseClass, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configurar la interfaz
        self.setWindowTitle("Slider de Imágenes")

        # Lista de imágenes
        self.images = [
            r"C:\Users\Manuel\Desktop\PIP_2025_1_Eq0\archivos\kevin.jpg", r"C:\Users\Manuel\Desktop\PIP_2025_1_Eq0\archivos\kevin y ed.jpg",
            r"C:\Users\Manuel\Desktop\PIP_2025_1_Eq0\archivos\geto.jpg", r"C:\Users\Manuel\Desktop\PIP_2025_1_Eq0\archivos\mishi.jpg",
            r"C:\Users\Manuel\Desktop\PIP_2025_1_Eq0\archivos\miles.jpg",
            r"C:\Users\Manuel\Desktop\PIP_2025_1_Eq0\archivos\peso.jpg", r"C:\Users\Manuel\Desktop\PIP_2025_1_Eq0\archivos\fi.jpg",
            r"C:\Users\Manuel\Desktop\PIP_2025_1_Eq0\archivos\Papel.jpg", r"C:\Users\Manuel\Desktop\PIP_2025_1_Eq0\archivos\Piedra.jpg"
        ]

        # Ajustar el rango del slider al número de imágenes
        self.SelectorImagen.setRange(0, len(self.images) - 1)  # Rango de 0 a 8 (9 imágenes)

        # Conectar el slider a la función que cambia la imagen
        self.SelectorImagen.valueChanged.connect(self.update_image)

        # Inicializar con la primera imagen
        self.update_image()

    def update_image(self):
        # Obtener el índice de la imagen según el valor del slider
        image_index = self.SelectorImagen.value()

        # Cargar la imagen correspondiente
        pixmap = QPixmap(self.images[image_index])

        # Actualizar el QLabel con la nueva imagen
        self.Imagen_Descripcion.setPixmap(pixmap.scaled(self.Imagen_Descripcion.size(), Qt.KeepAspectRatio))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
