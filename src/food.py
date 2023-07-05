from random import randint
from pygame import draw as pg_draw
from .global_vars import *


class Apple:

    def __init__(self):
        self.generate_new_position(
            exception_positions=[(GRID_WIDTH//2, GRID_HEIGHT//2)]
        )
    
    def generate_new_position(self, exception_positions=[]):
        generate=True
        while generate:
            x_new_pos = randint(0, GRID_WIDTH-1)
            y_new_pos = randint(0, GRID_HEIGHT-1)

            if (x_new_pos, y_new_pos) not in exception_positions:
                self.position = (x_new_pos, y_new_pos)
                generate=False

    def draw(self, surface):
        x_window_pos = self.position[0]*CELL_SIZE
        y_window_pos = self.position[1]*CELL_SIZE

        pg_draw.rect(
            surface,
            APPLE_COLOR,
            (
                x_window_pos,
                y_window_pos,
                CELL_SIZE,
                CELL_SIZE,
            )
        )
