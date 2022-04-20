import sys

from PyQt5.QtWidgets import QApplication

from tetris_gui import Tetris

if __name__ == "__main__":
    app = QApplication([])
    sample_tetris = Tetris(ai="bruh", speed=500)
    sample_tetris.tetris_board.board_coordinate[2][19] = 1
    sample_tetris.tetris_board.board_coordinate[3][19] = 1

    sample_tetris.tetris_board.board_coordinate[4][19] = 1
    sample_tetris.tetris_board.board_coordinate[5][19] = 1
    sample_tetris.tetris_board.board_coordinate[6][19] = 1
    sample_tetris.tetris_board.board_coordinate[7][19] = 1
    sample_tetris.tetris_board.board_coordinate[8][19] = 1
    sample_tetris.tetris_board.board_coordinate[9][19] = 1

    sample_tetris.tetris_board.board_coordinate[2][18] = 1
    sample_tetris.tetris_board.board_coordinate[3][18] = 1
    sample_tetris.tetris_board.board_coordinate[4][18] = 1
    sample_tetris.tetris_board.board_coordinate[5][18] = 1
    sample_tetris.tetris_board.board_coordinate[6][18] = 1
    sample_tetris.tetris_board.board_coordinate[7][18] = 1
    sample_tetris.tetris_board.board_coordinate[8][18] = 1
    sample_tetris.tetris_board.board_coordinate[9][18] = 1

    sample_tetris.tetris_board.current_piece = "O_piece"
    sys.exit(app.exec_())
