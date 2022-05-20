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

        if ai is None:
            self.tetris_board = model.Board()
        else:
            self.tetris_board = ai_model.AI()

        self.height = grid_size * (self.tetris_board.height - self.tetris_board.top_offset)
        self.width = grid_size * self.tetris_board.width

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

        self.update()

    def timerEvent(self, event: QTimerEvent):

        if type(self.tetris_board) == tetris_ai.AI:
            self.tetris_board.scan_lines()
            list_coordinates = []
            for i in range(10):
                list_coordinates.append([i, 22])
                list_coordinates.append([i, 21])
                list_coordinates.append([i, 20])
                list_coordinates.append([i, 19])
            self.tetris_board.heuristic_board_reachability_search(list_coordinates)
            # self.tetris_board.reachability_dfs()

        self.tetris_board.move_down()

        self.update()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        color = QColor("blue")
        # draw board
        for i in range(self.tetris_board.width):
            for j in range(self.tetris_board.top_offset, self.tetris_board.height):
                if self.tetris_board.board_coordinate[i][j] == 1:
                    painter.fillRect(i * self.grid_size, (j - self.tetris_board.top_offset) * self.grid_size,
                                     self.grid_size, self.grid_size, color)
        # draw current piece
        color = QColor("blue")
        for coordinate_x, coordinate_y in self.tetris_board.get_current_piece_coordinate():
            painter.fillRect(coordinate_x * self.grid_size, (coordinate_y - self.tetris_board.top_offset) * self.grid_size,
                             self.grid_size, self.grid_size, color)

    # def draw_piece(self, coordinate, color):
    #     painter = QPainter(self)
    #     color = QColor(color)
    #     for coordinate_x, coordinate_y in coordinate:
    #         painter.fillRect(coordinate_x * self.grid_size,
    #                          (coordinate_y - self.tetris_board.top_offset) * self.grid_size,
    #                          self.grid_size, self.grid_size, color)
    #     self.update()


if __name__ == "__main__":
    app = QApplication([])
    tetris = Tetris(grid_size=20)
    sys.exit(app.exec_())
