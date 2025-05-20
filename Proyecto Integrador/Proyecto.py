import sys
import serial
import serial.tools.list_ports
import threading
import keyboard
import time
from PyQt5 import QtWidgets, uic, QtCore

class ControlApp(QtWidgets.QMainWindow):
    actualizar_lecturas = QtCore.pyqtSignal(str)
    actualizar_acciones = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        uic.loadUi("Proyecto.ui", self)

        self.lecturas_txt = self.findChild(QtWidgets.QTextEdit, "lecturas_txt")
        self.acciones_txt = self.findChild(QtWidgets.QTextEdit, "acciones_txt")

        self.actualizar_lecturas.connect(self.update_lecturas)
        self.actualizar_acciones.connect(self.update_acciones)

        # Bloquear escritura en los QTextEdit
        self.lecturas_txt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.acciones_txt.setFocusPolicy(QtCore.Qt.NoFocus)

        self.arduino = self.detectar_arduino()

        # Estado de la dirección anterior
        self.direccion_actual = None

        if self.arduino:
            self.listener_thread = threading.Thread(target=self.listen_serial, daemon=True)
            self.listener_thread.start()
        else:
            self.lecturas_txt.append("Arduino no encontrado.")

    def detectar_arduino(self):
        ports = list(serial.tools.list_ports.comports())
        for port in ports:
            if "Arduino" in port.description or "CH340" in port.description or "USB-SERIAL" in port.description:
                try:
                    arduino = serial.Serial(port.device, 9600, timeout=1)
                    return arduino
                except serial.SerialException:
                    pass
        return None

    def listen_serial(self):
        while True:
            if self.arduino.in_waiting > 0:
                data = self.arduino.readline().decode('utf-8').strip()
                print(f"Recibido: {data}")

                direcciones = ["Arriba ↑", "Abajo ↓", "Izquierda ←", "Derecha →"]

                if data in direcciones:
                    self.actualizar_lecturas.emit(data)

                    if self.direccion_actual != data:
                        if self.direccion_actual:
                            tecla_anterior = self.traducir_direccion_a_tecla(self.direccion_actual)
                            keyboard.release(tecla_anterior)

                        tecla_nueva = self.traducir_direccion_a_tecla(data)
                        keyboard.press(tecla_nueva)
                        self.direccion_actual = data

                elif data in ["Pulsador A", "Pulsador B", "Pulsador C", "Pulsador D"]:
                    self.actualizar_acciones.emit(data)

                    # Asignar teclas: A = z, B = x, C = c, D = v
                    teclas = {
                        "Pulsador A": 'z',
                        "Pulsador B": 'x',
                        "Pulsador C": 'c',
                        "Pulsador D": 'v'
                    }
                    tecla = teclas.get(data)
                    keyboard.press(tecla)
                    time.sleep(0.40)
                    keyboard.release(tecla)

                elif data == "Centro":
                    if self.direccion_actual:
                        tecla = self.traducir_direccion_a_tecla(self.direccion_actual)
                        keyboard.release(tecla)
                        self.direccion_actual = None

    def traducir_direccion_a_tecla(self, direccion):
        return {
            "Arriba ↑": "up",
            "Abajo ↓": "down",
            "Izquierda ←": "left",
            "Derecha →": "right"
        }[direccion]

    def update_lecturas(self, texto):
        self.lecturas_txt.append(texto)

    def update_acciones(self, texto):
        self.acciones_txt.append(texto)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ControlApp()
    window.show()
    window.setFocus()
    sys.exit(app.exec_())
