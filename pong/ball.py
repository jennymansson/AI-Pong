import pygame
import math
import random

"""
Blueprint for a ball
It defines how that ball behaves and keeps track of its position on the screen
"""
class Ball:
    MAX_VELOCITY = 10
    RADIUS = 8

    # Initialization of a new ball 
    def __init__(self, x, y):
        self.x = self.original_x = x
        self.y = self.original_y = y
        
        # Generates a random angle within the range of -30 and 30 degrees (converted to radians)
        angle = math.radians(random.uniform(-30, 30))

        # Determines direction randomly 
        pos = 1 if random.random() < 0.5 else -1

        # Calculate initial celovities based on angle and direction 
        self.x_velocity = pos * abs(math.cos(angle) * self.MAX_VELOCITY)
        self.y_velocity = math.sin(angle) * self.MAX_VELOCITY

    # Function for drawing the ball on the game window 
    def draw(self, window):
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), self.RADIUS)

    # Function for moving the ball 
    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

    # Function to reset the ball to default position 
    # (but in the opposite direction as last time)
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

        angle = math.radians(random.uniform(-30, 30))
        x_velocity = abs(math.cos(angle) * self.MAX_VELOCITY)
        y_velocity = math.sin(angle) * self.MAX_VELOCITY

        self.y_velocity = y_velocity
        self.x_velocity *= -1
