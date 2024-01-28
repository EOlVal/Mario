import pygame
from Tiles import AnimatedTile
from support import import_folder


class Upper(AnimatedTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, '../pics/ladder')
        self.speed = 1

    def move(self):
        self.rect.y += self.speed

    def reverse_speed(self):
        self.speed = -self.speed
        self.rect.y += self.speed

    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
