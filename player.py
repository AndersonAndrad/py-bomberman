import pygame

class Player:
    def __init__(self, game_map):
        self.map = game_map
        self.tile_size = self.map.title_size
        self.x = 1
        self.y = 1

    def move(self, dx, dy):
        new_x, new_y = self.x + dx, self.y + dy

        # Check if the new position is walkable (only walk on '1')
        if self.map.map[new_y][new_x] == 1:
            self.x = new_x
            self.y = new_y

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x * self.tile_size, self.y * self.tile_size, self.tile_size, self.tile_size))
