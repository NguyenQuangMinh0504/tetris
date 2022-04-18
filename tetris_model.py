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
            [[0, 0], [1, 0], [1, 1], [2, 1]], [[0, 1], [0, 2], [1, 0], [1, 1]],
            [[0, 0], [1, 0], [1, 1], [2, 1]], [[0, 1], [0, 2], [1, 0], [1, 1]]
        ],
        'O_piece': [
            [[0, 0], [0, 1], [1, 0], [1, 1]], [[0, 0], [0, 1], [1, 0], [1, 1]],
            [[0, 0], [0, 1], [1, 0], [1, 1]], [[0, 0], [0, 1], [1, 0], [1, 1]]
        ],
        'L_piece': [
            [[0, 0], [0, 1], [1, 0], [2, 0]], [[0, 0], [0, 1], [0, 2], [1, 2]],
            [[0, 1], [1, 1], [2, 0], [2, 1]], [[0, 0], [1, 0], [1, 1], [1, 2]]
        ],
        'I_piece': [
            [[0, 0], [1, 0], [2, 0], [3, 0]], [[0, 0], [0, 1], [0, 2], [0, 3]],
            [[0, 0], [1, 0], [2, 0], [3, 0]], [[0, 0], [0, 1], [0, 2], [0, 3]]
        ],
        'S_piece': [
            [[0, 1], [1, 0], [1, 1], [2, 0]], [[0, 0], [0, 1], [1, 1], [1, 2]],
            [[0, 1], [1, 0], [1, 1], [2, 0]], [[0, 0], [0, 1], [1, 1], [1, 2]]
        ]
    }

    piece_name = list(piece_coordinate.keys())

    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.board_coordinate = [[0] * self.height for i in range(self.width)]
        self.current_piece_x = 4
        self.current_piece_y = 0
        self.current_rotate_offset = 0
        self.current_piece = random.choice(self.piece_name)
        self.next_piece = random.choice(self.piece_name)

    def move_down(self):
        if self.check_move_availability(move_down=1):
            self.current_piece_y += 1
        else:
            # fix the piece if it no can no longer be moved
            for x, y in self.get_current_piece_coordinate():
                self.board_coordinate[x][y] = 1
            # generate next piece
            self.current_piece = self.next_piece
            self.next_piece = random.choice(self.piece_name)
            self.current_rotate_offset = 0
            self.current_piece_x = 4
            self.current_piece_y = 0
            # check for lines clear
            self.clear_lines()

    def move(self, direction):
        k = -1 if direction == "left" else 1
        if self.check_move_availability(move_direction=k):
            self.current_piece_x += k

    def rotate(self, direction):
        k = 1 if direction == "left" else - 1 if direction == "right" else 0
        if self.check_move_availability(rotate_direction=k):
            self.current_rotate_offset = (self.current_rotate_offset + k) % 4

    def get_current_piece_coordinate(self, rotate_direction=0, move_direction=0, move_down=0):
        piece_coordinate_in_board = []
        for x, y in self.piece_coordinate[self.current_piece][(self.current_rotate_offset + rotate_direction) % 4]:
            piece_coordinate_in_board.append([x + self.current_piece_x + move_direction,
                                              y + self.current_piece_y + move_down])
        return piece_coordinate_in_board

    def check_move_availability(self, rotate_direction=0, move_direction=0, move_down=0):
        for x, y in self.get_current_piece_coordinate(rotate_direction=rotate_direction,
                                                      move_direction=move_direction,
                                                      move_down=move_down):
            if x >= 10 or x <= -1:
                return False
            if y >= 20:
                return False
            if self.board_coordinate[x][y] == 1:
                return False
        return True

    def clear_lines(self):
        y = 19
        while y != 0:
            if sum(self.board_coordinate[x][y] for x in range(10)) == 10:
                for j in range(y, 0, -1):
                    for x in range(10):
                        self.board_coordinate[x][j] = self.board_coordinate[x][j-1]
                y = 19
            else:
                y -= 1
