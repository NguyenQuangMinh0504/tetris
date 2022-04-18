import random

from tetris_model import Board


class AI(Board):
    def __init__(self):
        super().__init__()

    def random_move(self):
        random_direction = random.choice(["left", "right", "no move"])
        print(random_direction)
        super().move(direction=random_direction)

    def random_rotate(self):
        random_direction = random.choice(["left", "right", "no move"])
        super().rotate(direction=random_direction)




