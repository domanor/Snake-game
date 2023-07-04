import pygame
from global_vars import *
from snake import *

def main(window):

    pygame.init()
    pygame.display.set_caption('game SNAKE')

    snake = Snake()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()



if __name__ == '__main__':
    my_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    main(my_window)
