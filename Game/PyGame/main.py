import pygame, sys
from support import *
from settings import *
from level_1 import Level_1
from level_2 import Level_2
from level_3 import Level_3
from game_data import level_1, level_2, level_3
import const as c
import datetime as dt

pygame.init()
pygame.display.set_caption('Mario')
pygame_icon = pygame.image.load('../icon/icon.png')
pygame.display.set_icon(pygame_icon)
size = screen_width, screen_height
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
level_1 = Level_1(level_1, screen)
level_2 = Level_2(level_2, screen)
level_3 = Level_3(level_3, screen)


def goodbye():
    while 1:
        for ev in pygame.event.get():
            if ev.type in [pygame.QUIT, pygame.KEYDOWN]:
                pygame.quit()
                exit()
        draw_text(screen, "ЧТОБЫ ВЫЙТИ НАЖМИТЕ ЛЮБУЮ КЛАВИШУ", c.font_mid, (110, 20, 219), screen_width // 2, 67)
        pygame.display.flip()


def lose():
    while 1:
        for ev in pygame.event.get():
            if ev.type in [pygame.QUIT, pygame.KEYDOWN]:
                pygame.quit()
                exit()
        draw_text(screen, "ВЫ ПРОИГРАЛИ", c.font_mid, (255, 0, 0), screen_width // 2, 40)
        draw_text(screen, f"РЕЗУЛЬТАТ: {c.COUNT} ОЧКОВ", c.font_mid, (255, 255, 255), screen_width // 2, 80)
        draw_text(screen, "ЧТОБЫ ВЫЙТИ НАЖМИТЕ ЛЮБУЮ КЛАВИШУ", c.font_mid, (110, 20, 219), screen_width // 2, 160)
        pygame.display.flip()


def win():
    while 1:
        for ev in pygame.event.get():
            if ev.type in [pygame.QUIT, pygame.KEYDOWN]:
                pygame.quit()
                exit()
        draw_text(screen, "ВЫ ВЫИГРАЛИ", c.font_mid, c.GREEN, screen_width // 2, 40)
        draw_text(screen, f'РЕЗУЛЬТАТ: {c.COUNT} ОЧКОВ', c.font_mid, (255, 255, 255), screen_width // 2, 80)
        pygame.display.flip()


def pause():
    run = True
    while run:
        if c.ESC:
            pygame.mixer.music.pause()
            draw_text(screen, "ПАУЗА", c.font_mid, c.GREEN, screen_width // 2, 40)
            draw_text(screen, "НАЖМИТЕ ENTER ЧТОБЫ ВЕРНУТЬСЯ В ИГРУ", c.font_mid, (255, 0, 0), screen_width // 2, 106)
            pygame.display.flip()
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    run = False
                    c.ESC = False
                    pygame.mixer.music.unpause()
                elif ev.key == pygame.K_1:
                    top_score()


def intro():
    run = True
    while run:
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    run = False
                elif ev.key == pygame.K_ESCAPE:
                    screen.fill('black')
                    goodbye()
            elif ev.type == pygame.QUIT:
                pygame.quit()
                exit()

        draw_text(screen, "НАЖМИТЕ SPACE ЧТОБЫ НАЧАТЬ ИГРУ", c.font_mid, (0, 0, 255), screen_width // 2, 67)
        pygame.display.flip()


intro()
if c.NUMB_LEVEL == 1:
    pygame.mixer.music.load('../soundtrack/underground.mp3')

elif c.NUMB_LEVEL == 2:
    pygame.mixer.music.load('../soundtrack/super-mario-saundtrek.mp3')

if c.PLAY:
    pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.mixer.music.stop()
        elif event.type == pygame.K_ESCAPE:
            running = False
            screen.fill('black')
            goodbye()

        elif c.LIVES == 0:
            running = False
            pygame.mixer.music.stop()
            c.death.play()
            screen.fill('black')
            lose()

        elif c.WIN:
            running = False
            pygame.mixer.music.stop()
            c.win.play()
            screen.fill('black')
            win()

        while c.ESC:
            pygame.mixer.music.pause()
            c.pause.play()
            screen.fill('grey')
            pause()

    if c.NUMB_LEVEL == 1:
        c.vertical_tile_number = 12
        screen.fill('#6495ED')
        level_1.run()

    elif c.NUMB_LEVEL == 2:
        c.vertical_tile_number = 12
        screen.fill('black')
        level_2.run()

    elif c.NUMB_LEVEL == 3:
        c.vertical_tile_number = 17
        screen.fill('#6495ED')
        level_3.run()

    text = c.font_mid.render(f'Очков: {c.COUNT}', True, c.WHITE)
    rect = text.get_rect()
    screen.blit(text, (100, 10), rect)
    pygame.display.update()
    clock.tick(c.FPS)
pygame.quit()
