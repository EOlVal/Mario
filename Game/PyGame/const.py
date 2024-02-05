import sqlite3

import pygame

WORLD_SHIFT = 0
COUNT_COINS = 0
COUNT_LUCKY_BL = 0
COUNT = 0
LIVES = 3
NUMB_LEVEL = 1

CHECK_WIN = False
COUNT_RED_F = 0
FPS = 60

WHITE = (255, 255, 255)
MAGENTA = (255, 0, 255)
pygame.font.init()
font_mid = pygame.font.Font("../font/Peace_Sans.ttf", 40)

vertical_tile_number = 17

WIN = False
ESC = False

BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 120, 64)
YELLOW = (255, 224, 160)
TRANSP = (116, 172, 255)

pygame.mixer.init()
PLAY = True

coin = pygame.mixer.Sound('../soundtrack/coin.mp3')
coin.set_volume(50)

death = pygame.mixer.Sound('../soundtrack/mario-smert.mp3')
death.set_volume(50)

win = pygame.mixer.Sound('../soundtrack/win.mp3')
win.set_volume(70)

jump = pygame.mixer.Sound('../soundtrack/jump.mp3')
jump.set_volume(50)

red_fung = pygame.mixer.Sound('../soundtrack/fung_red.mp3')
red_fung.set_volume(90)

pause = pygame.mixer.Sound('../soundtrack/pause.mp3')
pause.set_volume(80)

fung = pygame.mixer.Sound('../soundtrack/fung.mp3')
fung.set_volume(70)

path = '../pics/funguses/level_1'
