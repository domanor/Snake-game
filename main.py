import pygame

from src.direction import Direction
import src.food 
import src.const as CONST
import src.snake


running = False

def loop(window, snake, apple):
    global running

    snake.move()
    
    if snake.is_collision():
        running = False
    
    head_position = snake.body[0]
    if head_position == apple.position:
        snake.grow()
        apple.generate_new_position()

    window.fill(CONST.BACKGROUND_COLOR)
    snake.draw(window)
    apple.draw(window)
    pygame.display.update()


def main(window):
    global running

    pygame.init()

    snake = src.snake.Snake()
    apple = src.food.Apple()
    clock = pygame.time.Clock()

    running = True
    is_pressed_key = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN and is_pressed_key == False:

                if event.key == pygame.K_w and snake.direction != Direction.down:
                    snake.direction = Direction.up
                    is_pressed_key = True

                elif event.key == pygame.K_s and snake.direction != Direction.up:
                    snake.direction = Direction.down
                    is_pressed_key = True

                elif event.key == pygame.K_a and snake.direction != Direction.right:
                    snake.direction = Direction.left
                    is_pressed_key = True

                elif event.key == pygame.K_d and snake.direction != Direction.left:
                    snake.direction = Direction.right
                    is_pressed_key = True
        
        loop(window, snake, apple)
        is_pressed_key = False

        clock.tick(CONST.FPS)    

    pygame.quit()


if __name__ == '__main__':
    my_window = pygame.display.set_mode(
        (CONST.WINDOW_WIDTH, CONST.WINDOW_HEIGHT)
    )
    pygame.display.set_caption('SNAKE')

    main(my_window)
