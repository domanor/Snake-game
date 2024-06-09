from pygame import draw as pygame_draw

from src.direction import Direction, shifts_in_directions
import src.const as CONST
from src.position import Position

class Snake:

    def __init__(self):
        self.body = [CONST.START_POSITION]
        self.direction = Direction.right
    

    def is_collision(self):
        head_position = self.body[0]
        return head_position in self.body[1:]


    def move(self):
        dx, dy = shifts_in_directions[self.direction]
        head_position = self.body[0]

        new_position = Position(
            head_position.x + dx,
            head_position.y + dy
        )

        if new_position.x == -1:
            new_position.x = CONST.GRID_WIDTH - 1

        elif new_position.x == CONST.GRID_WIDTH:
            new_position.x = 0

        elif new_position.y == -1:
            new_position.y = CONST.GRID_HEIGHT - 1

        elif new_position.y == CONST.GRID_HEIGHT:
            new_position.y = 0

        self.body.insert(0, new_position)
        self.body.pop()


    def grow(self, increase=1):
        tail_position = self.body[-1]
        increased_tail = [tail_position]*increase

        self.body.extend(increased_tail)
    

    def draw(self, surface):
        for cell_snake_position in self.body:
            window_position = cell_snake_position*CONST.CELL_SIZE

            pygame_draw.rect(
                surface, 
                CONST.SNAKE_COLOR, 
                (   
                    window_position.x, 
                    window_position.y, 
                    CONST.CELL_SIZE, 
                    CONST.CELL_SIZE
                )
            )

