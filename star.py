from pygame import Surface
from pygame.draw import ellipse
from random import randint
from constants import *


class Star:
    def __init__(self):
        self.reset_coordinates()

    def reset_coordinates(self):
        self.x = randint(-SCREEN_WIDTH, SCREEN_WIDTH)
        self.y = randint(-SCREEN_HEIGHT, SCREEN_HEIGHT)
        self.z = randint(SCREEN_WIDTH // 4, SCREEN_WIDTH)

    def update(self):
        self.z -= 10
        if self.z < SCREEN_WIDTH // 4:
            self.reset_coordinates()

    def draw(self, surface: Surface):
        center_y = SCREEN_HEIGHT // 2
        star_x = (self.x / self.z) * center_y + center_y
        star_y = (self.y / self.z) * center_y + center_y
        t = inverser_lerp(self.z, center_y / 2, SCREEN_HEIGHT)
        r = 1 * (1 - t) + 5 * t
        c = int(255 * t), int(150 * t), int(100 * t)
        ellipse(surface, (c), (star_x, star_y, r, r))


def inverser_lerp(v: float, start: float, end: float) -> float:
    return (v - start) / (end - start)
