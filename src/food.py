import random

from pygame import draw as pygame_draw

import src.const as CONST
from src.position import Position


class Apple:

    def __init__(self):
        self.generate_new_position(
            exception_positions=[CONST.START_POSITION]
        )
    

    def generate_new_position(self, exception_positions=[]):
        generate=True
        while generate:
            new_position = Position(
                random.randint(0, CONST.GRID_WIDTH-1),
                random.randint(0, CONST.GRID_HEIGHT-1)
            )

            if new_position not in exception_positions:
                self.position = new_position
                generate=False


    def draw(self, surface):
        window_position = self.position*CONST.CELL_SIZE

        pygame_draw.rect(
            surface,
            CONST.APPLE_COLOR,
            (
                window_position.x,
                window_position.y,
                CONST.CELL_SIZE,
                CONST.CELL_SIZE,
            )
        )
