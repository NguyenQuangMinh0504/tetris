from tetris_model import Board


class AI(Board):
    def __init__(self):
        super().__init__()

    # def foo(self, list_coordinates):
    #     move = []
    #     for i in self.reachability_coordinate(list_coordinates):
    #         for j in i[1]:
    #             if j:
    #                 move = i
    #                 print(i)
    #                 break
    #
    #     rotate_need = 0
    #     try:
    #         rotate_need = move[0] - self.current_rotate_index
    #     except IndexError:
    #         pass
    #     if rotate_need > 0:
    #         self.rotate(direction="left")
    #     elif rotate_need < 0:
    #         self.rotate(direction="right")
    #     else:
    #         pass
    #     try:
    #         for i in move[1]:
    #             if i:
    #                 self.move(direction=i[0])
    #     except TypeError:
    #         pass
    #     except IndexError:
    #         pass

    # def reachability_coordinate(self, list_coordinates):
    #     reachability_coordinates = []
    #     for rotate_index in range(len(self.piece_coordinate[self.current_piece])):
    #         current_reach_coordinate = []
    #         for coordinates in list_coordinates:
    #             current_reach_coordinate.append(
    #                 self.heuristic_coordinate_reachability_search(coordinate=coordinates, rotate_index=rotate_index)
    #             )
    #         reachability_coordinates.append([rotate_index, current_reach_coordinate])
    #     return reachability_coordinates

    def heuristic_board_reachability_search(self, list_coordinates):
        empty_search_board = [[False] * self.height for _ in range(self.width)]
        for i in range(self.height):
            print("Line {}".format(i), end="\t")
            for j in range(self.width):
                print(empty_search_board[j][i], end="\t")
            print("")

        for coordinate in list_coordinates:
            coordinate_reachability = self.heuristic_coordinate_reachability_search(coordinate)
            if coordinate_reachability:
                empty_search_board[coordinate[0]][coordinate[1]] = coordinate_reachability

        for i in range(self.height):
            print("Line {}".format(i), end="\t")
            for j in range(self.width):
                print(empty_search_board[j][i], end="\t")
            print("")

    def a_star_coordinate_reachability_search(self, coordinate):
        pass

    def heuristic_coordinate_reachability_search(self, coordinate):
        reachability = True
        for rotate_index in range(len(self.piece_coordinate[self.current_piece])):
            reachability = True
            # get the board coordinate of the assumption piece
            piece_coordinate = self.get_piece_coordinate(self.current_piece, rotate_index, coordinate[0], coordinate[1])

            # check if the piece is fit first
            if not self.check_fit_availability(coordinate=piece_coordinate):
                print("can not fit the piece !")
                reachability = False

            # check if can reach the piece on time
            x_distance = self.current_piece_coordinate_x - coordinate[0]
            y_distance = self.current_piece_coordinate_y - coordinate[1]
            if (abs(x_distance) - abs(y_distance)) > 0:
                print("can not reach the piece on time")
                reachability = False

            # check if piece can reach the target (# in case of blocking on the way)
            for i in range(1, x_distance + 1, 1):
                moving_coordinate = []
                for x, y in self.piece_coordinate[self.current_piece][self.current_rotate_index]:

                    if x_distance > 0:
                        x += self.current_piece_coordinate_x - i
                    if x_distance < 0:
                        x += self.current_piece_coordinate_x + i
                    y += self.current_piece_coordinate_y + i
                    moving_coordinate.append([x, y])
                if not self.check_fit_availability(coordinate=moving_coordinate):
                    print("can not reach the coordinate because the piece is block on the way")
                    reachability = False

            # check if the piece can move down
            piece_coordinate = [[x, y + 1] for x, y in piece_coordinate]
            if self.check_fit_availability(piece_coordinate):
                print("the piece can still move down")
                reachability = False

            if reachability:
                return True

        # if x_distance > 0:
        #     return ["left"] * abs(x_distance)
        # elif x_distance < 0:
        #     return ["right"] * abs(x_distance)
        # else:
        #     pass
        return reachability

    def non_recursive_depth_first_search(self, current_piece, current_rotate_index,
                                         current_coordinate, destination_coordinate):
        visited = [[0] * self.height for _ in range(self.width)]

        if not self.check_legit_coordinate(current_coordinate):
            return False

        stack = [current_coordinate]
        visited[current_coordinate[0]][current_coordinate[1]] = "start"

        while stack:
            coordinate = stack.pop(0)
            if visited[coordinate[0]][coordinate[1]] == 0:
                visited[coordinate[0]][coordinate[1]] = [[coordinate[0], coordinate[1] - 1], "no move"]
                if self.check_fit_availability(
                        self.get_piece_coordinate(current_piece, current_rotate_index,
                                                  coordinate[0], coordinate[1])):
                    if coordinate[0] == destination_coordinate[0] and coordinate[1] == destination_coordinate[1]:
                        print("found")
                        self.print_board(visited)
                        return visited
                    else:
                        child_coordinate = [coordinate[0], coordinate[1] + 1]
                        if self.check_legit_coordinate(child_coordinate):
                            stack.insert(0, child_coordinate)

            move_left_coordinate = [coordinate[0] - 1, coordinate[1]]

            if self.check_legit_coordinate(move_left_coordinate):
                if visited[move_left_coordinate[0]][move_left_coordinate[1]] == 0:
                    visited[move_left_coordinate[0]][move_left_coordinate[1]] = [coordinate, "left"]
                    if self.check_fit_availability(
                            self.get_piece_coordinate(current_piece, current_rotate_index,
                                                      move_left_coordinate[0], move_left_coordinate[1])):
                        if move_left_coordinate[0] == destination_coordinate[0]\
                                and move_left_coordinate[1] == destination_coordinate[1]:
                            print("found")
                            self.print_board(visited)
                            return visited
                        else:
                            child_move_left_coordinate = [move_left_coordinate[0], move_left_coordinate[1] + 1]
                            if self.check_legit_coordinate(child_move_left_coordinate):
                                stack.insert(0, child_move_left_coordinate)

            move_right_coordinate = [coordinate[0] + 1, coordinate[1]]
            if self.check_legit_coordinate(move_right_coordinate):
                if visited[move_right_coordinate[0]][move_right_coordinate[1]] == 0:
                    visited[move_right_coordinate[0]][move_right_coordinate[1]] = [coordinate, "right"]
                    if self.check_fit_availability(
                            self.get_piece_coordinate(current_piece, current_rotate_index,
                                                      move_right_coordinate[0], move_right_coordinate[1])):
                        if move_right_coordinate[0] == destination_coordinate[0] \
                                and move_right_coordinate[1] == destination_coordinate[1]:
                            print("found")
                            self.print_board(visited)
                            return visited
                        else:
                            child_move_right_coordinate = [move_right_coordinate[0], move_right_coordinate[1] + 1]
                            if self.check_legit_coordinate(child_move_right_coordinate):
                                stack.insert(0, child_move_right_coordinate)

    def scan_lines(self):
        for y in range(self.height - 1, -1, -1):
            empty_cells = []
            empty_cell_count = 0
            for x in range(self.width):
                if self.board_coordinate[x][y] == 0:
                    empty_cells.append([x, y])
                    empty_cell_count += 1
            break
