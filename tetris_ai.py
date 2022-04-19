import random

from tetris_model import Board


class AI(Board):
    def __init__(self):
        super().__init__()

    def random_move(self):
        random_direction = random.choice(["left", "right", "no move"])
        super().move(direction=random_direction)

    def random_rotate(self):
        random_direction = random.choice(["left", "right", "no move"])
        super().rotate(direction=random_direction)

    def reachability(self):
        coordinate = [0, 4]
        piece_coordinate = []
        for x, y in (self.piece_coordinate[self.current_piece][self.current_rotate_offset]):
            piece_coordinate.append([x + coordinate[0], y + coordinate[1]])
        if self.check_fit_availability(piece_coordinate):
            print("can fit to the board")
        else:
            print("can not fit to the board")

        x_distance = self.current_piece_coordinate_x - coordinate[0]
        y_distance = self.current_piece_coordinate_y - coordinate[1]
        reach_on_time = False
        if (abs(x_distance) - abs(y_distance)) > 0:
            print("cant reach the destination coordinate on time")
        else:
            reach_on_time = True
            print("can reach the destination one time")

        if x_distance > 0:
            self.move(direction="left")
        elif x_distance < 0:
            self.move(direction="right")
        else:
            pass

    def scan_lines(self):
        for y in range(self.height - 1, -1, -1):
            empty_cells = []
            empty_cell_count = 0
            for x in range(self.width):
                if self.board_coordinate[x][y] == 0:
                    empty_cells.append([x, y])
                    empty_cell_count += 1
            break










