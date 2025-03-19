import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap

qtCreatorFile = "E13_ContadorClicks.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class ClickCounterApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnStart.clicked.connect(self.start_timer)
        self.btnClick.clicked.connect(self.count_click)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        self.time_left = 10  # Segundos del contador
        self.click_count = 0

        self.lblImage.setPixmap(QPixmap("manoicono.png"))  # Carga la imagen
        self.lblImage.setScaledContents(True)  # Ajusta la imagen al QLabel

        self.update_labels()

    def start_timer(self):
        self.time_left = 10
        self.click_count = 0
        self.update_labels()

        self.btnClick.setEnabled(True)
        self.timer.start(1000)  # 1000 ms = 1 segundo

    def count_click(self):
        if self.time_left > 0:
            self.click_count += 1
            self.update_labels()

    def update_time(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.update_labels()
        if self.time_left == 0:
            self.timer.stop()
            self.btnClick.setEnabled(False)

    def update_labels(self):
        self.lblTime.setText(f"Tiempo: {self.time_left} s")
        self.lblClicks.setText(f"Clics: {self.click_count}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ClickCounterApp()
    window.show()
    sys.exit(app.exec())
