from tetris_model import Board


class AI(Board):
    def __init__(self):
        super().__init__()

    def foo(self, list_coordinates):
        move = []
        for i in self.reach_coordinate(list_coordinates):
            for j in i[1]:
                if j:
                    move = i
                    print(i)
                    break

        rotate_need = 0
        try:
            rotate_need = move[0] - self.current_rotate_index
        except IndexError:
            pass
        if rotate_need > 0:
            self.rotate(direction="left")
        elif rotate_need < 0:
            self.rotate(direction="right")
        else:
            pass
        try:
            for i in move[1]:
                if i:
                    self.move(direction=i[0])
        except TypeError:
            pass
        except IndexError:
            pass

    def reach_coordinate(self, list_coordinates):
        list_reach = []
        for rotate_index in range(len(self.piece_coordinate[self.current_piece])):
            current_reach_coordinate = []
            for coordinates in list_coordinates:
                current_reach_coordinate.append(self.reachability(coordinate=coordinates, rotate_index=rotate_index))
            list_reach.append([rotate_index, current_reach_coordinate])
        return list_reach

    def reachability(self, coordinate, rotate_index):
        # get the board coordinate of the assumption piece
        piece_coordinate = []
        for x, y in (self.piece_coordinate[self.current_piece][rotate_index]):
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
            for x, y in self.piece_coordinate[self.current_piece][self.current_rotate_index]:

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
            return ["left"] * abs(x_distance)
        elif x_distance < 0:
            return ["right"] * abs(x_distance)
        else:
            pass
        return True

    def reachability_dfs(self):
        reachability_tetris_board = [[0] * self.height for _ in range(self.width)]
        print(self.current_piece_coordinate_x, self.current_piece_coordinate_y)

        for rotate in range(-1, 2):
            print("current rotate index is: ", rotate)
            for move in range(-1, 2):
                print("current move is:", move)
                coordinate_x = self.current_piece_coordinate_x + move
                rotate_index = \
                    (self.current_rotate_index + rotate) % len(self.piece_coordinate[self.current_piece])
                coordinate_y = self.current_piece_coordinate_y + 1

                coordinate = self.get_piece_coordinate(piece=self.current_piece,
                                                       rotate_index=rotate_index,
                                                       coordinate_x=coordinate_x,
                                                       coordinate_y=coordinate_y)

                if self.check_fit_availability(coordinate=coordinate):
                    reachability_tetris_board[coordinate_x][coordinate_y] = [rotate, move]
        print(reachability_tetris_board[self.top_offset])
        print(reachability_tetris_board[self.top_offset + 1])
        print(reachability_tetris_board[self.top_offset + 2])
        print(reachability_tetris_board[self.top_offset + 3])
        print(reachability_tetris_board[self.top_offset + 4])
        print(reachability_tetris_board[self.top_offset + 5])


    def scan_lines(self):
        for y in range(self.height - 1, -1, -1):
            empty_cells = []
            empty_cell_count = 0
            for x in range(self.width):
                if self.board_coordinate[x][y] == 0:
                    empty_cells.append([x, y])
                    empty_cell_count += 1
            break
