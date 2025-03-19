from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer, QTime
from PyQt5 import uic
import sys
import recursos_rc

class RelojAlarma(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("E11_Reloj_con_Alarma.ui", self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_hora)
        self.timer.start(1000)  # Actualiza cada segundo
        self.alarma_activada = False
        self.btn_alarma.clicked.connect(self.toggle_alarma)


        self.hora_alarma = QTime(0, 0, 0)
        self.actualizar_label_hora_alarma()


        self.btn_hora_up.clicked.connect(self.aumentar_hora)
        self.btn_hora_down.clicked.connect(self.disminuir_hora)
        self.btn_minutos_up.clicked.connect(self.aumentar_minutos)
        self.btn_minutos_down.clicked.connect(self.disminuir_minutos)
        self.btn_segundos_up.clicked.connect(self.aumentar_segundos)
        self.btn_segundos_down.clicked.connect(self.disminuir_segundos)

    def actualizar_hora(self):
        hora_actual = QTime.currentTime()
        self.lcd_hora.display(hora_actual.toString("hh:mm:ss"))
        if self.alarma_activada:
            if self.hora_alarma <= hora_actual.addSecs(1) and self.hora_alarma >= hora_actual.addSecs(-1):
                print("¡Alarma!")
                self.alarma_activada = False
                self.btn_alarma.setText("Activar Alarma")

    def toggle_alarma(self):
        self.alarma_activada = not self.alarma_activada
        if self.alarma_activada:
            self.btn_alarma.setText("Desactivar Alarma")
        else:
            self.btn_alarma.setText("Activar Alarma")

    def actualizar_label_hora_alarma(self):

        hora_str = self.hora_alarma.toString("hh:mm:ss")
        self.label_hora_alarma.setText(hora_str)

    def aumentar_hora(self):
        hora = self.hora_alarma.hour()
        hora = (hora + 1) % 24
        self.hora_alarma.setHMS(hora, self.hora_alarma.minute(), self.hora_alarma.second())
        self.actualizar_label_hora_alarma()

    def disminuir_hora(self):
        hora = self.hora_alarma.hour()
        hora = (hora - 1) % 24
        self.hora_alarma.setHMS(hora, self.hora_alarma.minute(), self.hora_alarma.second())
        self.actualizar_label_hora_alarma()

    def aumentar_minutos(self):
        minutos = self.hora_alarma.minute()
        minutos = (minutos + 1) % 60
        self.hora_alarma.setHMS(self.hora_alarma.hour(), minutos, self.hora_alarma.second())
        self.actualizar_label_hora_alarma()

    def disminuir_minutos(self):
        minutos = self.hora_alarma.minute()
        minutos = (minutos - 1) % 60
        self.hora_alarma.setHMS(self.hora_alarma.hour(), minutos, self.hora_alarma.second())
        self.actualizar_label_hora_alarma()

    def aumentar_segundos(self):
        segundos = self.hora_alarma.second()
        segundos = (segundos + 1) % 60
        self.hora_alarma.setHMS(self.hora_alarma.hour(), self.hora_alarma.minute(), segundos)
        self.actualizar_label_hora_alarma()

    def disminuir_segundos(self):
        segundos = self.hora_alarma.second()
        segundos = (segundos - 1) % 60
        self.hora_alarma.setHMS(self.hora_alarma.hour(), self.hora_alarma.minute(), segundos)
        self.actualizar_label_hora_alarma()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    reloj = RelojAlarma()
    reloj.show()
    sys.exit(app.exec_())
