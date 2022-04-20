import sys

from PyQt5.QtCore import QBasicTimer, QTimerEvent

import tetris_ai
import tetris_model as model
import tetris_ai as ai_model
from PyQt5.QtGui import QPainter, QColor, QPaintEvent, QKeyEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame


class Board(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(600, 300)
        self.show()


class Tetris(QMainWindow):
    def __init__(self, grid_size=20, ai=None, speed=100):
        super().__init__()
        # set up the timer
        self.timer = QBasicTimer()
        self.timer.start(speed, self)

        self.grid_size = grid_size
        self.height = grid_size * 20
        self.width = grid_size * 10

        if ai is None:
            self.tetris_board = model.Board()
        else:
            self.tetris_board = ai_model.AI()

        self.init_ui()
        self.show()

    def init_ui(self):
        self.setWindowTitle("Tetris")

        self.setFixedSize(self.width, self.height)

    def keyPressEvent(self, event: QKeyEvent):
        if event.text() == "k":
            self.tetris_board.move(direction="right")
        elif event.text() == "h":
            self.tetris_board.move(direction="left")
        elif event.text() == "a":
            self.tetris_board.rotate(direction="left")
        elif event.text() == "d":
            self.tetris_board.rotate(direction="right")

    def timerEvent(self, event: QTimerEvent):

        if type(self.tetris_board) == tetris_ai.AI:
            self.tetris_board.scan_lines()
            list_coordinates = []
            for i in range(10):
                list_coordinates.append([i, 19])
                list_coordinates.append([i, 18])
            self.tetris_board.foo(list_coordinates)

        self.tetris_board.move_down()

        self.update()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        color = QColor("blue")
        # draw board
        for i in range(10):
            for j in range(20):
                if self.tetris_board.board_coordinate[i][j] == 1:
                    painter.fillRect(i * self.grid_size, j * self.grid_size,
                                     self.grid_size, self.grid_size, color)
        # draw current piece
        for coordinate_x, coordinate_y in self.tetris_board.get_piece_coordinate():
            painter.fillRect(coordinate_x * self.grid_size, coordinate_y * self.grid_size,
                             self.grid_size, self.grid_size, color)


if __name__ == "__main__":
    app = QApplication([])
    tetris = Tetris(grid_size=20)
    sys.exit(app.exec_())
