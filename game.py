import sys
import pygame
from map import *  # Importing everything from map.py
from player import *
from bomb import *
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("2D Game")
        self.clock = pygame.time.Clock()
        self.running = True

        self.map = Map()  # Initialize the map
        self.player = Player(self.map)  # Initialize the player
        self.bombs = []  # Initialize bombs list
        self.explosions = []  # Initialize explosions list

    def run(self):
        while self.running:
            self.handle_events()  # Handle keyboard input
            self.update()  # Update game logic
            self.draw()  # Render everything

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

    def handle_events(self):
        """Handles player input and events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_LEFT:
                    self.player.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.move(1, 0)
                elif event.key == pygame.K_UP:
                    self.player.move(0, -1)
                elif event.key == pygame.K_DOWN:
                    self.player.move(0, 1)
                elif event.key == pygame.K_SPACE:
                    self.bombs.append(Bomb(self.player.x, self.player.y))  # Drop bomb

    def update(self):
        """Handles game updates like explosions"""
        for bomb in self.bombs[:]:
            if bomb.has_exploded():
                self.explosions.append((bomb.x, bomb.y))
                self.bombs.remove(bomb)

    def draw(self):
        """Draws all game elements"""
        self.screen.fill(BLACK)
        self.map.draw(self.screen)
        self.player.draw(self.screen)

        # Draw bombs
        for bomb in self.bombs:
            bomb.draw(self.screen)

        # Draw explosions
        for explosion in self.explosions[:]:
            pygame.draw.rect(
                self.screen, RED,
                (explosion[0] * GRID_SIZE, explosion[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            )
            self.explosions.remove(explosion)

if __name__ == "__main__":
    Game().run()
