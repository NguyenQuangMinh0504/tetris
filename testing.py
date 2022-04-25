import sys

from PyQt5.QtWidgets import QApplication

from tetris_gui import Tetris

if __name__ == "__main__":
    app = QApplication([])
    sample_tetris = Tetris(ai=None, speed=3000)
    for i in range(10):

        sample_tetris.tetris_board.board_coordinate[i][-1] = 1
        sample_tetris.tetris_board.board_coordinate[i][-2] = 1
        sample_tetris.tetris_board.board_coordinate[i][-3] = 1

    sample_tetris.tetris_board.board_coordinate[4][-2] = 0
    sample_tetris.tetris_board.board_coordinate[4][-1] = 0
    sample_tetris.tetris_board.board_coordinate[5][-2] = 0
    sample_tetris.tetris_board.board_coordinate[5][-1] = 0
    sample_tetris.tetris_board.board_coordinate[4][-3] = 0
    sample_tetris.tetris_board.board_coordinate[5][-3] = 0
    sample_tetris.tetris_board.board_coordinate[3][-1] = 0

    sample_tetris.tetris_board.board_coordinate[0][-6] = 1
    sample_tetris.tetris_board.board_coordinate[1][-6] = 1
    sample_tetris.tetris_board.board_coordinate[2][-6] = 1
    sample_tetris.tetris_board.board_coordinate[3][-6] = 1
    sample_tetris.tetris_board.board_coordinate[4][-6] = 1
    sample_tetris.tetris_board.board_coordinate[5][-6] = 1
    sample_tetris.tetris_board.board_coordinate[6][-6] = 1


    sample_tetris.tetris_board.current_piece = "J_piece"
    sys.exit(app.exec_())
