import pygame

from snake_app import Grid, Snake
from snake_app.cartesian import Direction
from settings import settings

def main():
    
    #initialize the grid the game will be modelled from
    grid = Grid(settings['grid_size'], settings['block_width'], settings['block_padding'])

    #pygame setup
    screen = pygame.display.set_mode(grid.screen_size)
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    running = True

    #initialize the snake
    snake = Snake(settings['grid_size'], settings['start_length'])
    snake.start_state()
    move = snake.direction
    speed = settings['speed']

    while running:

        #stops from pressing twice in one frame and then moving in forbidden directions
        key_pressed = False

        for event in pygame.event.get():
            #so can quit
            if event.type == pygame.QUIT: 
                running = False
                break
            
            #change direction (in allowed directions)
            if event.type == pygame.KEYDOWN:
                if not key_pressed:
                    key_pressed = True

                    if event.key == pygame.K_UP:
                        move = Direction.N
                    elif event.key == pygame.K_RIGHT:
                        move = Direction.E
                    elif event.key == pygame.K_DOWN:
                        move = Direction.S
                    elif event.key == pygame.K_LEFT:
                        move = Direction.W

        #move in the chosen direction
        snake.move(move)

        #check if we've died
        if snake.is_dead:
            running = False
            break

        #fill the screen to wipe last frame
        screen.fill((40,40,40))

        #visualize the snake and food on the screen
        pygame.draw.rect(screen, 'red', pygame.Rect(grid.gridpoint_to_coordinates(snake.target.position), (grid.block_width, grid.block_width)))
        for pos in snake.body:
            pygame.draw.rect(screen, 'green', pygame.Rect(grid.gridpoint_to_coordinates(pos), (grid.block_width, grid.block_width)))

        #display the changes
        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()