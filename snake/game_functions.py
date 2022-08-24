import sys
import pygame
import constants as cte


#controla os eventos do game
class Game_Function():
    def __init__(self, snake, apple):
        self.snake = snake
        self.apple = apple
        self.game_over = False
        self.score = 0

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.moviment_up = True

                if event.key == pygame.K_RIGHT:
                    self.snake.moviment_right = True

                if event.key == pygame.K_DOWN:
                    self.snake.moviment_down = True

                if event.key == pygame.K_LEFT:
                    self.snake.moviment_left = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.snake.moviment_up = False

                if event.key == pygame.K_RIGHT:
                    self.snake.moviment_right = False

                if event.key == pygame.K_DOWN:
                    self.snake.moviment_down = False

                if event.key == pygame.K_LEFT:
                    self.snake.moviment_left = False

    def update(self):
        self.snake.move_snake()
        if Game_Function.eat_apple(self):
            self.snake.snake.append((0,0))
            self.apple.apple_pos = self.apple.on_grid_random()
            self.score += 10
            print("score =", self.score, end = "\r")
        Game_Function.colision_snake_snake(self)
        Game_Function.colision_snake_wall(self)

    def eat_apple(self):
        return self.snake.snake[0] == self.apple.apple_pos

    def colision_snake_snake(self):
        for i in range(1, len(self.snake.snake)):
            if self.snake.snake[i] == self.snake.snake[0]:
                self.game_over = True

    def colision_snake_wall(self):
        if self.snake.snake[0][0] == cte.width or self.snake.snake[0][0] == 0:
            self.game_over = True

        if self.snake.snake[0][1] ==  cte.high or self.snake.snake[0][1] == 0:
            self.game_over = True
