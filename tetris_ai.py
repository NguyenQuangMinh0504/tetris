from tetris_model import Board


class AI(Board):
    def __init__(self):
        super().__init__()

    def foo(self, list_coordinates):
        move = []
        for i in self.reach_coordinate(list_coordinates):
            if i:
                move = i
                break
        try:
            print(self.reach_coordinate(list_coordinates))
            self.move(direction=move[0])
        except IndexError:
            pass
        except TypeError:
            pass

    def reach_coordinate(self, list_coordinates):
        list_reach = []
        foo = []
        for coordinates in list_coordinates:
            list_reach.append(self.reachability(coordinate=coordinates))
        if list_reach == foo:
            print(list_coordinates)
        return list_reach

    def reachability(self, coordinate):
        # get the board coordinate of the assumption piece
        piece_coordinate = []
        for x, y in (self.piece_coordinate[self.current_piece][self.current_rotate_offset]):
            piece_coordinate.append([x + coordinate[0], y + coordinate[1]])

        # check if the piece is fit first
        if not self.check_fit_availability(coordinate=piece_coordinate):
            return False

        # check if can reach the piece on time
        x_distance = self.current_piece_coordinate_x - coordinate[0]
        y_distance = self.current_piece_coordinate_y - coordinate[1]
        if (abs(x_distance) - abs(y_distance)) > 0:
            return False

        # check if piece can reach the target (# in case of blocking on the way)
        for i in range(1, x_distance + 1, 1):
            coordinate = []
            for x, y in self.piece_coordinate[self.current_piece][self.current_rotate_offset]:

                if x_distance > 0:
                    x += self.current_piece_coordinate_x - i
                if x_distance < 0:
                    x += self.current_piece_coordinate_x + i
                y += self.current_piece_coordinate_y + i

                coordinate.append([x, y])
            if not self.check_fit_availability(coordinate=coordinate):
                return False

        # check if the piece can move down
        piece_coordinate = [[x, y + 1] for x, y in piece_coordinate]
        if self.check_fit_availability(piece_coordinate):
            return False

        if x_distance > 0:
            return["left"] * abs(x_distance)
        elif x_distance < 0:
            return ["right"] * abs(x_distance)
        else:
            pass
        return True

    def scan_lines(self):
        for y in range(self.height - 1, -1, -1):
            empty_cells = []
            empty_cell_count = 0
            for x in range(self.width):
                if self.board_coordinate[x][y] == 0:
                    empty_cells.append([x, y])
                    empty_cell_count += 1
            break
