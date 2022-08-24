#verifica o andamento do game
import pygame
import snake_settings
import apple_settings


class Game_status():

    def __init__(self, snake, apple_pos):
        self.snake = snake
        self.apple_pos = apple_pos
        self.game_over = False

    def colision_eat_apple(self):
        if self.snake[0] == self.apple_pos:
            self.snake.append((0,0))
            
