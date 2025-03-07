import pygame

class Player:
    def __init__(self, game_map):
        self.map = game_map
        self.tile_size = self.map.title_size
        self.position_x = 1
        self.position_y = 1

    def move(self, direction_x, direction_y):
        new_position_x= self.position_x + direction_x
        new_position_y = self.position_y + direction_y

        if self.map.map[new_position_y][new_position_x] == 1:
            self.position_x = new_position_x
            self.position_y = new_position_y

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.position_x * self.tile_size, self.position_y * self.tile_size, self.tile_size, self.tile_size))
