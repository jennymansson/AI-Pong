import pygame

""" 
Blueprint for a paddle
It defines how that paddle behaves and keeps track of its position on the screen 
"""
class Paddle:
    VELOCITY = 4
    WIDTH = 20
    HEIGHT = 100

    # Initialization of a new paddle 
    def __init__(self, x, y):
        self.x = self.default_x = x
        self.y = self.default_y = y

    # Function for drawing the paddle on the game window 
    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), 
                        (self.x, self.y, self.WIDTH, self.HEIGHT))

    # Function for moving the paddle up and down 
    def move(self, up = True):
        if up:
            self.y -= self.VELOCITY
        else:
            self.y += self.VELOCITY

    # Function to reset the paddle to default position 
    def reset(self):
        self.x = self.default_x
        self.y = self.default_y
