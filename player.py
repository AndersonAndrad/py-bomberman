import pygame

class Player:
    def __init__(self, game_map):
        self.map = game_map
        self.tile_size = self.map.title_size
        self.position_x = 1
        self.position_y = 1

    def move(self, event):
        new_position_x = self.position_x
        new_position_y = self.position_y

        if event.key == pygame.K_LEFT:
            new_position_x -= 1
        elif event.key == pygame.K_RIGHT:
            new_position_x += 1
        elif event.key == pygame.K_UP:
            new_position_y -= 1
        elif event.key == pygame.K_DOWN:
            new_position_y += 1

        if self.map.is_walkable(new_position_x, new_position_y):
            self.position_x = new_position_x
            self.position_y = new_position_y

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.position_x * self.tile_size, self.position_y * self.tile_size, self.tile_size, self.tile_size))


