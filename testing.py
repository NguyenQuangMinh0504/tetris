import sys

from PyQt5.QtWidgets import QApplication

from tetris_gui import Tetris

if __name__ == "__main__":
    app = QApplication([])
    sample_tetris = Tetris(ai="bruh", speed=3000)
    for i in range(10):

        sample_tetris.tetris_board.board_coordinate[i][-1] = 1
        sample_tetris.tetris_board.board_coordinate[i][-2] = 1
        sample_tetris.tetris_board.board_coordinate[i][-3] = 1
        sample_tetris.tetris_board.board_coordinate[i][-4] = 1
        sample_tetris.tetris_board.board_coordinate[i][-5] = 1

    sample_tetris.tetris_board.board_coordinate[4][23] = 0
    sample_tetris.tetris_board.board_coordinate[4][22] = 0
    sample_tetris.tetris_board.board_coordinate[4][21] = 0
    sample_tetris.tetris_board.board_coordinate[4][20] = 0

    sample_tetris.tetris_board.board_coordinate[5][23] = 0
    sample_tetris.tetris_board.board_coordinate[5][22] = 0
    sample_tetris.tetris_board.board_coordinate[5][21] = 0
    sample_tetris.tetris_board.board_coordinate[5][20] = 0

    sample_tetris.tetris_board.board_coordinate[6][23] = 0
    sample_tetris.tetris_board.board_coordinate[6][22] = 0
    sample_tetris.tetris_board.board_coordinate[6][21] = 0
    sample_tetris.tetris_board.board_coordinate[6][20] = 0

    sample_tetris.tetris_board.board_coordinate[5][19] = 0

    sample_tetris.tetris_board.current_piece = "I_piece"
    sample_tetris.tetris_board.print_piece(sample_tetris.tetris_board.current_piece, 1, [5, 5])
    sample_tetris.tetris_board.non_recursive_depth_first_search(sample_tetris.tetris_board.current_piece, 1, [5, 5], [6, 20])

    # sys.exit(app.exec_())
