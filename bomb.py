import time
import pygame

import settings
from settings import *

class Bomb:
    def __init__(self, position_x, position_y, tile_size, game_map):
        self.position_x = position_x
        self.position_y = position_y
        self.tile_size = tile_size
        self.exploded = False
        self.start_time = time.time()
        self.explosion_duration = settings.EXPLOSION_DURATION
        self.game_map = game_map

    def update(self):
        if time.time() - self.start_time >= self.explosion_duration:
            self.exploded = True
            self.destroy_walls()

    def destroy_walls(self):
        for direction_x in [-1, 1]:
            if 0 <= self.position_x + direction_x < len(self.game_map.map[0]):
                if self.game_map.map[self.position_y][self.position_x + direction_x] == 2:
                    self.game_map.map[self.position_y][self.position_x + direction_x] = 1

        for direction_y in [-1, 1]:
            if 0 <= self.position_y + direction_y < len(self.game_map.map):
                if self.game_map.map[self.position_y + direction_y][self.position_x] == 2:
                    self.game_map.map[self.position_y + direction_y][self.position_x] = 1

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