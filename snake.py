import enum
import pygame
from global_vars import *


direction = enum.Enum(
    value='direction',
    names='up down left right',
)

class Snake:

    shifts_in_directions = {
        direction.up:   (0, -1),
        direction.down: (0, 1),
        direction.left: (-1, 0),
        direction.right:(1, 0),
    }

    def __init__(self):
        self.body = [(GRID_WIDTH//2, GRID_HEIGHT//2)]
        self.direction = direction.right
    
    def is_collision(self) -> bool:
        ...

    def move(self):
        ...
    
    def grow(self):
        ...
    
    def draw(self):
        ...