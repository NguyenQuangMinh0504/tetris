import sys

from PyQt5.QtWidgets import QApplication

from tetris_gui import Tetris

if __name__ == "__main__":
    app = QApplication([])
    sample_tetris = Tetris(ai="yes")

    for y in range(4, 20, 1):
        for x in range(9):
            sample_tetris.tetris_board.board_coordinate[x][y] = 1

    sample_tetris.tetris_board.board_coordinate[0][4] = 0
    sample_tetris.tetris_board.board_coordinate[1][4] = 0
    sample_tetris.tetris_board.board_coordinate[2][4] = 0
    sample_tetris.tetris_board.board_coordinate[3][4] = 0

    sample_tetris.tetris_board.board_coordinate[0][5] = 0
    sample_tetris.tetris_board.board_coordinate[1][5] = 0
    sample_tetris.tetris_board.board_coordinate[2][5] = 0
    sample_tetris.tetris_board.board_coordinate[3][5] = 0

    sample_tetris.tetris_board.current_piece = "O_piece"
    sys.exit(app.exec_())
