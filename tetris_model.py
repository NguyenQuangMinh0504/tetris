import random


class Board:
    piece_coordinate = {
        'T_piece': [
            [[0, 0], [1, 0], [1, 1], [2, 0]], [[0, 0], [0, 1], [0, 2], [1, 1]],
            [[0, 1], [1, 0], [1, 1], [2, 1]], [[0, 1], [1, 0], [1, 1], [1, 2]]
        ],
        'J_piece': [
            [[0, 0], [1, 0], [2, 0], [2, 1]], [[0, 0], [0, 1], [0, 2], [1, 0]],
            [[0, 0], [0, 1], [1, 1], [2, 1]], [[0, 2], [1, 0], [1, 1], [1, 2]]
        ],
        'Z_piece': [
            [[0, 0], [1, 0], [1, 1], [2, 1]], [[0, 1], [0, 2], [1, 0], [1, 1]]
        ],
        'O_piece': [
            [[0, 0], [0, 1], [1, 0], [1, 1]]
        ],
        'L_piece': [
            [[0, 0], [0, 1], [1, 0], [2, 0]], [[0, 0], [0, 1], [0, 2], [1, 2]],
            [[0, 1], [1, 1], [2, 0], [2, 1]], [[0, 0], [1, 0], [1, 1], [1, 2]]
        ],
        'I_piece': [
            [[0, 0], [1, 0], [2, 0], [3, 0]], [[0, 0], [0, 1], [0, 2], [0, 3]]
        ],
        'S_piece': [
            [[0, 1], [1, 0], [1, 1], [2, 0]], [[0, 0], [0, 1], [1, 1], [1, 2]]
        ]
    }

    piece_name = list(piece_coordinate.keys())

    def __init__(self, width=10, height=20):

        self.top_offset = 4  # define a top offset to enable L, J and I piece rotate at top

        # init height and width of the board
        self.width = width
        self.height = height + self.top_offset

        # init board coordinate
        self.board_coordinate = [[0] * self.height for _ in range(self.width)]

        # init piece
        self.current_piece = random.choice(self.piece_name)
        self.current_piece_coordinate_x = 4
        # self.current_piece_x = 4 means that the piece will spawn at the center of the board
        self.current_piece_coordinate_y = self.top_offset
        self.current_rotate_index = 0

        self.next_piece = random.choice(self.piece_name)

    def move_down(self):
        if self.check_fit_availability(
                self.get_piece_coordinate(piece=self.current_piece, rotate_index=self.current_rotate_index,
                                          coordinate_x=self.current_piece_coordinate_x,
                                          coordinate_y=self.current_piece_coordinate_y+1)
        ):
            self.current_piece_coordinate_y += 1
        else:
            # fix the piece if it no can no longer be moved
            for x, y in self.get_current_piece_coordinate():
                self.board_coordinate[x][y] = 1
            # generate next piece
            self.current_piece = self.next_piece
            self.next_piece = random.choice(self.piece_name)
            self.current_rotate_index = 0
            self.current_piece_coordinate_x = 4
            self.current_piece_coordinate_y = self.top_offset
            # check for lines clear
            self.clear_lines()

    def move(self, direction):
        k = -1 if direction == "left" else 1 if direction == "right" else 0 if direction == "no move" else None
        if self.check_fit_availability(
                self.get_piece_coordinate(piece=self.current_piece, rotate_index=self.current_rotate_index,
                                          coordinate_x=self.current_piece_coordinate_x + k,
                                          coordinate_y=self.current_piece_coordinate_y)
        ):
            self.current_piece_coordinate_x += k

    def rotate(self, direction):
        k = 1 if direction == "left" else - 1 if direction == "right" else 0 if direction == "no rotate" else None
        rotate_index = (self.current_rotate_index + k) % len(self.piece_coordinate[self.current_piece])
        if self.check_fit_availability(
                self.get_piece_coordinate(piece=self.current_piece, rotate_index=rotate_index,
                                          coordinate_x=self.current_piece_coordinate_x,
                                          coordinate_y=self.current_piece_coordinate_y)):
            self.current_rotate_index = (self.current_rotate_index + k) % len(self.piece_coordinate[self.current_piece])

    def get_piece_coordinate(self, piece, rotate_index, coordinate_x, coordinate_y):
        piece_coordinate_in_board = []
        for x, y in self.piece_coordinate[piece][rotate_index]:
            piece_coordinate_in_board.append([x + coordinate_x, y + coordinate_y])
        return piece_coordinate_in_board

    def get_current_piece_coordinate(self):
        return self.get_piece_coordinate(piece=self.current_piece, rotate_index=self.current_rotate_index,
                                         coordinate_x=self.current_piece_coordinate_x,
                                         coordinate_y=self.current_piece_coordinate_y)

    def check_fit_availability(self, coordinate, board=None):
        """
        return True if can fit, False if cant using board coordinates of the piece
        :param board:
        :param coordinate:
        :return:
        """
        if board is None:
            board = self.board_coordinate
        try:
            for x, y in coordinate:
                if x >= self.width or x <= -1:
                    return False
                if y >= self.height:
                    return False
                if board[x][y] == 1:
                    return False
            return True
        except TypeError:
            raise Exception("The coordinate {} is not in the right format".format(coordinate))

    def clear_lines(self):
        y = self.height - 1
        while y != 0:
            if sum(self.board_coordinate[x][y] for x in range(self.width)) == self.width:
                for j in range(y, 0, -1):
                    for x in range(self.width):
                        self.board_coordinate[x][j] = self.board_coordinate[x][j - 1]
                y = self.height - 1
            else:
                y -= 1

    def print_board(self):
        for i in range(self.height):
            print("Line {}".format(i), end="\t")
            for j in range(self.width):
                print(self.board_coordinate[j][i], end="\t")
            print("")

    def print_piece(self, piece, rotate_index, coordinate):
        new_board = self.board_coordinate.copy()
        for x, y in self.get_piece_coordinate(piece, rotate_index, coordinate[0], coordinate[1]):
            new_board[x][y] = 2

        for i in range(self.height):
            print("Line {}".format(i), end="\t")
            for j in range(self.width):
                print(new_board[j][i], end="\t")
            print("")







