import pygame
from Tiles import AnimatedTile
from support import import_folder


class Monster(AnimatedTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, '../pics/funguses')
        self.speed = 1

    def move(self):
        self.rect.x += self.speed

    def reverse(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def reverse_speed(self):
        self.speed = -self.speed
        self.rect.x += self.speed

    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverse()