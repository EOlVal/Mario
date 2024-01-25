import pygame
from support import import_folder


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, shift):
        self.rect.x += shift


class StatictTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface


class Fungus_red(StatictTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pygame.image.load('../pics/fungus_red.png').convert_alpha())


class Constraints(StatictTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pygame.image.load('../pics/constraint.jpg').convert_alpha())


class Cloud(StatictTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pygame.image.load('../pics/cloud.png'))


class Tree(StatictTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pygame.image.load('../pics/tree_2.png'))


class AnimatedTile(Tile):
    def __init__(self, size, x, y, path):
        super().__init__(size, x, y)
        self.frames = import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, shift):
        self.animate()
        self.rect.x += shift


class Coin(AnimatedTile):
    def __init__(self, size, x, y, path):
        super().__init__(size, x, y, path)


class Lucky_block(AnimatedTile):
    def __init__(self, size, x, y, path):
        super().__init__(size, x, y, path)
