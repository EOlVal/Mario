from csv import reader
from settings import *
from os import walk
import pygame
import const as c


def import_csv(path):
    platform_map = []
    with open(path) as map_level:
        level = reader(map_level, delimiter=',')
        for row in level:
            platform_map.append(list(row))
        return platform_map


def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / tile_size)
    tile_num_y = int(surface.get_size()[1] / tile_size)

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            new_surface = pygame.Surface((tile_size, tile_size), flags=pygame.SRCALPHA)
            new_surface.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
            cut_tiles.append(new_surface)
    return cut_tiles


def import_folder(path):
    surf_list = []
    for _, __, files in walk(path):
        for image in files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surf_list.append(image_surf)
    return surf_list


def draw_text(surf, text, font, color, x, y, centered=True):
    lines = text.split('\n')
    for i in range(len(lines)):
        text_surface = font.render(lines[i], True, color)
        text_rect = text_surface.get_rect()
        if centered:
            text_rect.midtop = (x, y + i * text_rect.height)
        else:
            text_rect.topleft = (x, y + i * text_rect.height)
        surf.blit(text_surface, text_rect)


def draw_value(surf, text, val, font, tcolor, vcolor, x, y):
    text_surface = font.render(text + ": ", True, tcolor)
    val_surface = font.render(str(val), True, vcolor)
    text_rect = text_surface.get_rect()
    val_rect = val_surface.get_rect()
    text_rect.topright = (x, y)
    val_rect.topleft = (x, y)
    surf.blit(text_surface, text_rect)
    surf.blit(val_surface, val_rect)


def top_score():
    x = [100, 150, 300, 350, 500]
    color = [c.BLUE, c.MAGENTA, c.GREEN, c.BLUE, c.MAGENTA]
    header = ["#", "Счет", "Уров", "   Дата", "Имя"]
    g.screen.fill(g.YELLOW)
    draw_text(g.screen, "Таблица рекордов", g.font_mid, g.BLUE, 150, 10, False)
    res = g.cur.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 20").fetchall()
    for j in range(1, 5):
        draw_text(g.screen, header[j], g.font_small, g.BLACK, x[j], 60, False)
    for i in range(len(res)):
        for j in range(1, 5):
            draw_text(g.screen, str(res[i][j]), g.font_small, color[j], x[j], i * 20 + 85, False)
    pygame.display.flip()
    run = True
    while run:
        g.clock.tick(g.FPS)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                goodbye()
            if ev.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                run = False
