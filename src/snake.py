from pygame import draw as pg_draw
from .dir import direction, shifts_in_directions
from .global_vars import *


class Snake:

    def __init__(self):
        self.body = [(GRID_WIDTH//2, GRID_HEIGHT//2)]
        self.direction = direction.right
    
    def is_collision(self) -> bool:
        head = self.body[0]
        if head in self.body[1:]:
            return True
        else:
            return False

    def move(self):
        dx, dy = shifts_in_directions[self.direction]

        x_new_pos = self.body[0][0] + dx
        y_new_pos = self.body[0][1] + dy

        if x_new_pos == -1:
            x_new_pos = GRID_WIDTH-1
        elif x_new_pos == GRID_WIDTH:
            x_new_pos = 0
        elif y_new_pos == -1:
            y_new_pos = GRID_HEIGHT-1
        elif y_new_pos == GRID_HEIGHT:
            y_new_pos = 0

        self.body.insert(0, (x_new_pos, y_new_pos))
        self.body.pop()

    def grow(self, increase=1):
        tail = self.body[-1]
        increased_tail = [tail]*increase

        self.body.extend(increased_tail)
    
    def draw(self, surface):
        for cell in self.body:
            x_window_pos = cell[0]*CELL_SIZE
            y_window_pos = cell[1]*CELL_SIZE

            pg_draw.rect(
                surface, 
                SNAKE_COLOR, 
                (   
                    x_window_pos, 
                    y_window_pos, 
                    CELL_SIZE, 
                    CELL_SIZE
                )
            )
