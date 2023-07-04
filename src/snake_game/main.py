import pygame
from global_vars import *
from snake import *
import food


running = None

def loop(window, snake, apple):
    global running

    snake.move()
    
    if snake.is_collision():
        running = False
    
    head_position = snake.body[0]
    if head_position == apple.position:
        snake.grow()
        apple.generate_new_position()

    window.fill(BACKGROUND_COLOR)
    snake.draw(window)
    apple.draw(window)
    pygame.display.update()


def main(window):
    global running

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
            
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w and snake.direction != direction.down:
                    snake.direction = direction.up
                elif event.key == pygame.K_s and snake.direction != direction.up:
                    snake.direction = direction.down
                elif event.key == pygame.K_a and snake.direction != direction.right:
                    snake.direction = direction.left
                elif event.key == pygame.K_d and snake.direction != direction.left:
                    snake.direction = direction.right
            
        loop(window, snake, apple)

        clock.tick(FPS)    
    pygame.quit()



if __name__ == '__main__':
    my_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    main(my_window)
