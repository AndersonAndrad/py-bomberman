import time
import pygame

import settings
from settings import *

class Bomb:
    def __init__(self, position_x, position_y, tile_size):
        self.position_x = position_x
        self.position_y = position_y
        self.tile_size = tile_size
        self.exploded = False
        self.start_time = time.time()
        self.explosion_duration = settings.EXPLOSION_DURATION

    def update(self):
        if time.time() - self.start_time >= self.explosion_duration:
            self.exploded = True

    def draw(self, screen):
        if not self.exploded:
            pygame.draw.circle(
                screen, (0,0,0),
                (
                    self.position_x * self.tile_size + self.tile_size // 2,
                    self.position_y * self.tile_size + self.tile_size // 2
                 ),
                self.tile_size // 3
            )