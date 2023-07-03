import enum
import pygame


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
        self.body = []
        self.direction = 'right'