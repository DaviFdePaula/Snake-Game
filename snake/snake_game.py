import pygame
import snake_settings
import apple_settings
import constants as cte
import game_functions

def run_game():
    pygame.init()
    screen = pygame.display.set_mode(cte.screen)
    snake = snake_settings.Snake_Settings(screen)
    apple = apple_settings.Apple_Settings(screen)
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    gf = game_functions.Game_Function(snake, apple)
    while True:
        if gf.game_over:
            break
        screen.fill(cte.bg_color)
        clock.tick(20)
        gf.check_events()
        gf.update()
        snake.blitme_snake()
        apple.blitme_apple()
        pygame.display.flip()
run_game()
