import pygame
import sys
from star import Star
from constants import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Starfield Simulation")
        self.clock = pygame.time.Clock()

        self.star_count = 2000
        self.star_group: list[Star] = [Star() for _ in range(self.star_count)]

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.screen.fill((0, 0, 0))
        for i in range(self.star_count):
            self.star_group[i].draw(self.screen)

        pygame.display.flip()

    def update(self):
        for i in range(self.star_count):
            self.star_group[i].update()
        if len(self.star_group) < 50:
            for i in range(self.star_count):
                self.star_group[i] = Star()

    def run(self):
        while True:
            self.handle_event()
            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
