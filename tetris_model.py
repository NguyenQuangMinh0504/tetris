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
        # init height and width of the board
        self.width = width
        self.height = height

        # init board coordinate
        self.board_coordinate = [[0] * self.height for _ in range(self.width)]

        # init piece
        self.current_piece = random.choice(self.piece_name)
        self.current_piece_coordinate_x = 4
        # self.current_piece_x = 4 means that the piece will spawn at the center of the board
        self.current_piece_coordinate_y = 0
        self.current_rotate_offset = 0

        self.next_piece = random.choice(self.piece_name)

    def move_down(self):
        if self.check_fit_availability(coordinate=self.get_piece_coordinate(move_down=1)):
            self.current_piece_coordinate_y += 1
        else:
            # fix the piece if it no can no longer be moved
            for x, y in self.get_piece_coordinate():
                self.board_coordinate[x][y] = 1
            # generate next piece
            self.current_piece = self.next_piece
            self.next_piece = random.choice(self.piece_name)
            self.current_rotate_offset = 0
            self.current_piece_coordinate_x = 4
            self.current_piece_coordinate_y = 0
            # check for lines clear
            self.clear_lines()

    def move(self, direction):
        k = -1 if direction == "left" else 1
        if self.check_fit_availability(coordinate=self.get_piece_coordinate(move_direction=k)):
            self.current_piece_coordinate_x += k

    def rotate(self, direction):
        k = 1 if direction == "left" else - 1 if direction == "right" else 0
        if self.check_fit_availability(coordinate=self.get_piece_coordinate(rotate_direction=k)):
            self.current_rotate_offset = \
                (self.current_rotate_offset + k) % len(self.piece_coordinate[self.current_piece])

    def get_piece_coordinate(self, rotate_direction=0, move_direction=0, move_down=0):

        """
        Return board coordinates of current piece

        :param rotate_direction: string "left" or "right", default 0 means no rotate
        :param move_direction: string "left" or "right", default 0 means no move
        :param move_down: 1 means move down, default 0 means no move
        :return: List of board coordinates of current piece
        """
        piece_coordinate_in_board = []
        for x, y in self.piece_coordinate[self.current_piece][(self.current_rotate_offset + rotate_direction) % len(self.piece_coordinate[self.current_piece])]:
            piece_coordinate_in_board.append([x + self.current_piece_coordinate_x + move_direction,
                                              y + self.current_piece_coordinate_y + move_down])
        return piece_coordinate_in_board

    def check_fit_availability(self, coordinate):
        """
        return True if can fit, False if cant using board coordinates of the piece
        :param coordinate:
        :return:
        """

        try:
            for x, y in coordinate:
                if x >= self.width or x <= -1:
                    return False
                if y >= self.height:
                    return False
                if self.board_coordinate[x][y] == 1:
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
