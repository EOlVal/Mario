import pygame, sys
from settings import *
from level import Level
from game_data import level_1

pygame.init()
size = screen_width, screen_height
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
level = Level(level_1, screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('#6495ED')
    level.run()

    pygame.display.update()
    clock.tick(60)
pygame.quit()
