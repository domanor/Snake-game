
class Direction:
    up = 1
    down = 2
    left = 3
    right = 4


shifts_in_directions = {
    Direction.up: (0, -1),
    Direction.down: (0, 1),
    Direction.left: (-1, 0),
    Direction.right: (1, 0),
}
