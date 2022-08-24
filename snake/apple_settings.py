import pygame
import random
import constants as cte

class Apple_Settings():
    def __init__(self, screen):
        self.screen = screen
        self.apple_pos = Apple_Settings.on_grid_random(self)
        self.apple = pygame.Surface(cte.block_size)
        self.apple.fill(cte.apple_color)

    def blitme_apple(self):
        self.screen.blit(self.apple, self.apple_pos)

    def on_grid_random(self):
        x = random.randint(0, cte.width -10)//10*10
        y = random.randint(0, cte.high - 10)//10*10
        return x, y
