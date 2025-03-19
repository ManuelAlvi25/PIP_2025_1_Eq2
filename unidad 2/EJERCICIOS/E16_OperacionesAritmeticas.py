import sys
import random
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E16_OperacionesAritmeticas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.tiempo_restante = 120
        self.aciertos = 0
        self.operacion_actual = ""
        self.resultado_correcto = 0

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.actualizar_tiempo)
        self.btn_confirmar.clicked.connect(self.verificar_respuesta)
        self.iniciar_juego()

    def iniciar_juego(self):
        self.timer.start(1000)
        self.nueva_operacion()

    def actualizar_tiempo(self):
        self.txt_tiempo.setText(str(self.tiempo_restante))
        if self.tiempo_restante == 0:
            self.timer.stop()
            QtWidgets.QMessageBox.information(self, "Fin del juego", f"Tiempo agotado. Aciertos: {self.aciertos}")
            self.close()
        self.tiempo_restante -= 1

    def nueva_operacion(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operacion = random.choice(["+", "-", "*"]) # se guarda en una lista las operaciones aritmeticas
        #la funcion random.choice selecciona uno al azar los que estan en esa lista y se lo asigna a la variable
        # operacion :D

        if operacion == "/":
            num1 = num1 * num2  # Asegurar divisiones exactas

        self.operacion_actual = f"{num1} {operacion} {num2}"
        self.resultado_correcto = eval(self.operacion_actual)

        self.txt_operaciones.setText(self.operacion_actual)
        self.respuesta.clear()  # Limpia la respuesta anterior

    def verificar_respuesta(self):
        respuesta_usuario = self.respuesta.text()
        if respuesta_usuario.isdigit() or (
                respuesta_usuario.replace(".", "", 1).isdigit() and "." in respuesta_usuario):
            if float(respuesta_usuario) == self.resultado_correcto:
                self.aciertos += 1  # Aumenta el conteo de aciertos
        self.nueva_operacion()  # Generar nueva operación


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
