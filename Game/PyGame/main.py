import pygame, sys
from settings import *
from level import Level_1, Level_2
from game_data import level_1, level_2
import const as c

pygame.init()
size = screen_width, screen_height
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
level_1 = Level_1(level_1, screen)
level_2 = Level_2(level_2, screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if c.NUMB_LEVEL == 1:
        screen.fill('#6495ED')
        level_1.run()

    elif c.NUMB_LEVEL == 2:
        screen.fill('black')
        level_2.run()

    elif c.NUMB_LEVEL == 3:
        screen.fill('#6495ED')

    pygame.display.update()
    clock.tick(60)
pygame.quit()
print(c.NUMB_LEVEL)
print(c.COUNT_RED_F)
