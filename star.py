from pygame import Surface
from pygame.draw import line
from random import randint
from constants import *


class Star:
    def __init__(self):
        self.reset_coordinates()

    def reset_coordinates(self):
        self.x = randint(-SCREEN_WIDTH, SCREEN_WIDTH)
        self.y = randint(-SCREEN_HEIGHT, SCREEN_HEIGHT)
        self.z = randint(SCREEN_WIDTH // 2, SCREEN_WIDTH)
        self.prev_z = self.z

    def update(self):
        self.prev_z = self.z
        self.z -= 30
        if self.z < SCREEN_WIDTH // 2:
            self.reset_coordinates()

    def draw(self, surface: Surface):
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        star_x = (self.x / self.z) * center_x + center_x
        star_y = (self.y / self.z) * center_y + center_y
        prev_star_x = (self.x / self.prev_z) * center_x + center_x
        prev_star_y = (self.y / self.prev_z) * center_y + center_y
        t = inverser_lerp(self.z, center_x, SCREEN_WIDTH)
        # radius = 1 * (1 - t) + 5 * t
        flicker = randint(-15, 15)

        r = max(0, min(255, int(255) + flicker))
        g = max(0, min(255, int(255 * t) + flicker))
        b = max(0, min(255, int(255 * t) + flicker))

        color = (r, g, b)

        line(surface, (color), (prev_star_x, prev_star_y), (star_x, star_y), 2)


def inverser_lerp(v: float, start: float, end: float) -> float:
    return (v - start) / (end - start)
