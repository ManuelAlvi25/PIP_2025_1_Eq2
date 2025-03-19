from PyQt5 import QtWidgets, QtGui, QtCore, uic
import random
import recursos_rc
import sys

class Memorama(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Proyecto.ui", self)

        self.btnReiniciar.setText("Iniciar")
        self.btnReiniciar.clicked.connect(self.iniciar_juego)
        self.pares = 5
        self.imagenes = [f"Imagen{i}.jpg" for i in range(1, self.pares + 1)] * 2
        self.botones = []
        self.seleccionadas = []
        self.intentos = 0
        self.tiempo = 0
        self.juego_iniciado = False
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.actualizar_tiempo)
        self.txtTiempo.setReadOnly(True)
        self.txtIntentos.setReadOnly(True)
        self.txtJuego.setReadOnly(True)
        self.txtTiempo.setText("0")
        self.txtIntentos.setText("0")
        self.txtJuego.setText("Inicio")
        self.crear_tablero()

    def crear_tablero(self):
        random.shuffle(self.imagenes)
        gridLayout = self.findChild(QtWidgets.QGridLayout, "gridLayout")
        while gridLayout.count():
            item = gridLayout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        self.botones = []
        for i in range(len(self.imagenes)):
            btn = QtWidgets.QPushButton()
            btn.setFixedSize(100, 100)
            btn.setIconSize(QtCore.QSize(90, 90))
            btn.setStyleSheet("border: 1px solid black;")
            btn.clicked.connect(lambda _, index=i: self.voltear(index))
            btn.setEnabled(False)
            self.botones.append(btn)
            gridLayout.addWidget(btn, i // self.pares, i % self.pares)

    def iniciar_juego(self):
        if not self.juego_iniciado:
            self.juego_iniciado = True
            self.btnReiniciar.setText("Reiniciar")
            self.txtJuego.setText("Jugando")
            self.timer.start(1000)
            for btn in self.botones:
                btn.setEnabled(True)
        else:
            self.reiniciar()

    def voltear(self, indice):
        if not self.juego_iniciado or len(self.seleccionadas) >= 2:
            return

        if self.botones[indice] not in self.seleccionadas:
            if not QtGui.QPixmap(self.imagenes[indice]).isNull():
                icono = QtGui.QIcon(self.imagenes[indice])
                self.botones[indice].setIcon(icono)
                self.seleccionadas.append(self.botones[indice])

        if len(self.seleccionadas) == 2:
            self.intentos += 1
            self.txtIntentos.setText(str(self.intentos))
            QtCore.QTimer.singleShot(1000, self.verificar_pareja)

    def verificar_pareja(self):
        if len(self.seleccionadas) < 2:
            return

        btn1, btn2 = self.seleccionadas
        idx1 = self.botones.index(btn1)
        idx2 = self.botones.index(btn2)

        if self.imagenes[idx1] != self.imagenes[idx2]:
            btn1.setIcon(QtGui.QIcon())
            btn2.setIcon(QtGui.QIcon())

        self.seleccionadas.clear()
        self.verificar_ganador()

    def actualizar_tiempo(self):
        if self.juego_iniciado:
            self.tiempo += 1
            self.txtTiempo.setText(str(self.tiempo))

    def verificar_ganador(self):
        if all(not btn.icon().isNull() for btn in self.botones):
            self.txtJuego.setText("Ganaste")
            self.timer.stop()

    def reiniciar(self):
        self.juego_iniciado = True
        random.shuffle(self.imagenes)
        self.seleccionadas.clear()
        self.intentos = 0
        self.tiempo = 0
        self.txtTiempo.setText("0")
        self.txtIntentos.setText("0")
        self.txtJuego.setText("Jugando")
        self.timer.start(1000)
        for btn in self.botones:
            btn.setIcon(QtGui.QIcon())
            btn.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Memorama()
    ventana.show()
    sys.exit(app.exec_())
