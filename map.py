import pygame
from settings import *

basic_map = [
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
        self.map = basic_map
        self.title_size = 50

        self.textures = {
            0: pygame.transform.scale(pygame.image.load('assets/textures/not-destructive-wall.png'), (self.title_size, self.title_size)),
            2: pygame.transform.scale(pygame.image.load('assets/textures/destructive-wall.png'), (self.title_size, self.title_size)),
        }

    def draw(self, screen):
        for position_y, row in enumerate(self.map):
            for position_x, col in enumerate(row):
               if col in self.textures:
                   screen.blit(self.textures[col], (position_x * self.title_size, position_y * self.title_size))
               else:
                   pygame.draw.rect(screen, (50, 100, 50), (position_x * self.title_size, position_y * self.title_size, self.title_size, self.title_size))