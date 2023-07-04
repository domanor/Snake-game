import pygame
from global_vars import *
from snake import *
import food


snake = None
apple = None
running = None

def loop(window):
    global running, snake, apple

    snake.move()
    
    window.fill(BACKGROUND_COLOR)
    snake.draw(window)
    apple.draw(window)
    pygame.display.update()


def main(window):
    global running, snake, apple

    pygame.init()
    pygame.display.set_caption('game SNAKE')

    snake = Snake()
    apple = food.Apple()
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        loop(window)

        clock.tick(FPS)    
    pygame.quit()



if __name__ == '__main__':
    my_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    main(my_window)
