import sys

from PyQt5.QtWidgets import QApplication

from tetris_gui import Tetris

if __name__ == "__main__":
    app = QApplication([])
    sample_tetris = Tetris(ai="bruh", speed=20000)

    sample_tetris.tetris_board.board_coordinate[0][-1] = 1
    sample_tetris.tetris_board.board_coordinate[1][-1] = 1
    sample_tetris.tetris_board.board_coordinate[2][-1] = 1
    sample_tetris.tetris_board.board_coordinate[3][-1] = 1

    sample_tetris.tetris_board.board_coordinate[7][-1] = 1
    sample_tetris.tetris_board.board_coordinate[8][-1] = 1
    sample_tetris.tetris_board.board_coordinate[9][-1] = 1

    sample_tetris.tetris_board.board_coordinate[0][-1] = 1
    sample_tetris.tetris_board.board_coordinate[1][-1] = 1
    sample_tetris.tetris_board.board_coordinate[2][-1] = 1
    sample_tetris.tetris_board.board_coordinate[3][-1] = 1
    sample_tetris.tetris_board.board_coordinate[4][-1] = 1
    sample_tetris.tetris_board.board_coordinate[7][-1] = 1
    sample_tetris.tetris_board.board_coordinate[8][-1] = 1
    sample_tetris.tetris_board.board_coordinate[9][-1] = 1

    sample_tetris.tetris_board.board_coordinate[0][-2] = 1
    sample_tetris.tetris_board.board_coordinate[1][-2] = 1
    sample_tetris.tetris_board.board_coordinate[2][-2] = 1
    sample_tetris.tetris_board.board_coordinate[3][-2] = 1
    sample_tetris.tetris_board.board_coordinate[4][-2] = 1
    sample_tetris.tetris_board.board_coordinate[7][-2] = 1
    sample_tetris.tetris_board.board_coordinate[8][-2] = 1
    sample_tetris.tetris_board.board_coordinate[9][-2] = 1
    #
    sample_tetris.tetris_board.current_piece = "I_piece"
    sys.exit(app.exec_())
