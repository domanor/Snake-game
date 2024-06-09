from src.position import Position


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BACKGROUND_COLOR = (180, 210, 255)
APPLE_COLOR = (200, 0, 0)          
SNAKE_COLOR = (0, 100, 0)           

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

#the cell size must be a multiple of the width and height of the window
CELL_SIZE = 30

GRID_WIDTH = WINDOW_WIDTH//CELL_SIZE
GRID_HEIGHT = WINDOW_WIDTH//CELL_SIZE
FPS = 15

START_POSITION = Position(GRID_WIDTH//2, GRID_HEIGHT//2)