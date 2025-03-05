import pygame
from settings import *

map = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,2,2,2,2,2,2,2,2,2,2,2,1,1,0],
    [0,1,0,2,0,2,0,2,0,2,0,2,0,2,0,1,0],
    [0,2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,0],
    [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
    [0,2,2,1,2,2,1,2,2,2,2,2,2,2,2,2,0],
    [0,2,0,2,0,2,0,2,0,1,0,2,0,2,0,2,0],
    [0,2,2,1,2,2,2,2,2,2,2,1,2,2,2,2,0],
    [0,1,0,2,0,2,0,2,0,2,0,2,0,2,0,1,0],
    [0,1,1,2,2,2,2,2,2,2,2,2,1,2,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

class Map:
    def __init__(self):
        self.map = map

        self.colors = {0: (200, 200, 200), 1: (50, 100, 50), 2: (0, 0, 255)}
        self.title_size = 50

    def draw(self, screen):
        for position_y, row in enumerate(self.map):
            for position_x, col in enumerate(row):
                pygame.draw.rect(screen, self.colors[col], (position_x * self.title_size, position_y * self.title_size, self.title_size, self.title_size))