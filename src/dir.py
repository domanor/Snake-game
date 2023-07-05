from enum import Enum


direction = Enum(
    value='direction',
    names='up down left right',
)

shifts_in_directions = {
    direction.up:   (0, -1),
    direction.down: (0, 1),
    direction.left: (-1, 0),
    direction.right:(1, 0),
}
