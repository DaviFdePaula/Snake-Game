import pygame
import numpy as np
import sys
import random
import constants as cte
import game_functions as gf


#controla as configurações da fruta
class Snake_Settings():
    def __init__(self, screen):
        self.screen = screen
        self.snake = [(cte.width//2, cte.high//2), (cte.width//2 + cte.block_size[0],
         cte.high//2),(cte.width//2 + 2*cte.block_size[0], cte.high//2)]
        self.snake_skin = pygame.Surface(cte.block_size)
        self.snake_skin.fill(cte.snake_color)

        #moviment Flag
        self.moviment_up = False
        self.moviment_right = False
        self.moviment_down = False
        self.moviment_left = False

    def move_snake(self):
        if self.moviment_up:
            self.snake.insert(0, (self.snake[0][0], self.snake[0][1] - cte.block_size[0]))
            self.snake.pop()
        if self.moviment_down:
            self.snake.insert(0, (self.snake[0][0], self.snake[0][1] + cte.block_size[0]))
            self.snake.pop()
        if self.moviment_right:
            self.snake.insert(0, (self.snake[0][0] + cte.block_size[0], self.snake[0][1]))
            self.snake.pop()
        if self.moviment_left:
            self.snake.insert(0,(self.snake[0][0] - cte.block_size[0], self.snake[0][1]))
            self.snake.pop()

    def blitme_snake(self):
        for pos in self.snake:
            self.screen.blit(self.snake_skin, pos)
