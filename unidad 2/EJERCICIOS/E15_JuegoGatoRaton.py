import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QGridLayout, QWidget
from PyQt5.uic import loadUi
import recursos_rc

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('E15_JuegoGatoRaton.ui', self)

        self.board = [None] * 9  # 9 casillas vacías
        self.turn = 'X'  # El jugador 'X' empieza
        self.game_over = False

        # Conectar los botones a una función
        self.btn_1.clicked.connect(lambda: self.make_move(0))
        self.btn_2.clicked.connect(lambda: self.make_move(1))
        self.btn_3.clicked.connect(lambda: self.make_move(2))
        self.btn_4.clicked.connect(lambda: self.make_move(3))
        self.btn_5.clicked.connect(lambda: self.make_move(4))
        self.btn_6.clicked.connect(lambda: self.make_move(5))
        self.btn_7.clicked.connect(lambda: self.make_move(6))
        self.btn_8.clicked.connect(lambda: self.make_move(7))
        self.btn_9.clicked.connect(lambda: self.make_move(8))
        # Conectar el botón de reinicio
        self.btn_reset.clicked.connect(self.reset_game)

    def make_move(self, index):
        if not self.game_over and self.board[index] is None:
            self.board[index] = self.turn
            self.update_button(index)
            if self.check_winner():
                self.statusLabel.setText(f"¡{self.turn} ha ganado!")
                self.game_over = True
            elif None not in self.board:
                self.statusLabel.setText("¡Es un empate!")
                self.game_over = True
            else:
                self.turn = 'O' if self.turn == 'X' else 'X'
                self.statusLabel.setText(f"Es el turno de {self.turn}")

    def update_button(self, index):
        button = getattr(self, f"btn_{index + 1}")
        button.setText(self.board[index])

    def check_winner(self):
        # Verificar las combinaciones ganadoras
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # filas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columnas
            (0, 4, 8), (2, 4, 6)  # diagonales
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != None:
                return True
        return False

    def reset_game(self):
        self.board = [None] * 9
        self.game_over = False
        self.turn = 'X'
        self.statusLabel.setText("¡Es tu turno! (X)")
        for i in range(9):
            button = getattr(self, f"btn_{i + 1}")
            button.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())
