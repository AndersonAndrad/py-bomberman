import sys
import pygame
from map import *
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

        self.map = Map()
        self.player = Player(self.map)

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.player.update()

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                else:
                    self.player.move(event)

    def draw(self):
        self.screen.fill(BLACK)
        self.map.draw(self.screen)
        self.player.draw(self.screen)

if __name__ == "__main__":
    Game().run()
