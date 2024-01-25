import pygame
from support import *
from settings import *
from Tiles import Tile, StatictTile, Lucky_block, Coin, Cloud, Tree, Fungus_red, Constraints
from monster import Monster
from player import Player


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.world_shift = 0

        self.COUNT_COINS = 0
        self.COUNT_LUCKY_BL = 0

        self.lives = 3

        player_layout = import_csv(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

        platforms_layout = import_csv(level_data['platforms'])
        self.platform_sprites = self.create_tile_group(platforms_layout, 'platforms')

        pipes_layout = import_csv(level_data['pipes'])
        self.pipes_sprites = self.create_tile_group(pipes_layout, 'pipes')

        lucky_blocks_layout = import_csv(level_data['lucky_blocks'])
        self.lucky_blocks_sprites = self.create_tile_group(lucky_blocks_layout, 'lucky_blocks')

        coins_layout = import_csv(level_data['coins'])
        self.coins_sprites = self.create_tile_group(coins_layout, 'coins')

        fungus_red_layout = import_csv(level_data['funguses_red'])
        self.fungus_red_sprites = self.create_tile_group(fungus_red_layout, 'funguses_red')

        trees_layout = import_csv(level_data['trees'])
        self.trees_sprites = self.create_tile_group(trees_layout, 'trees')

        castle_layout = import_csv(level_data['castle'])
        self.castle_sprites = self.create_tile_group(castle_layout, 'castle')

        mountains_layout = import_csv(level_data['mountains'])
        self.mountains_sprites = self.create_tile_group(mountains_layout, 'mountains')

        clouds_layout = import_csv(level_data['clouds'])
        self.clouds_sprites = self.create_tile_group(clouds_layout, 'clouds')

        monsters_layout = import_csv(level_data['monsters'])
        self.monsters_sprites = self.create_tile_group(monsters_layout, 'monsters')

        constraints_layout = import_csv(level_data['constraints'])
        self.constraints_sprites = self.create_tile_group(constraints_layout, 'constraints')

    def create_tile_group(self, layout, type_):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type_ == 'platforms':
                        platforms_tile_list = import_cut_graphics('../pics/platforms.jpg')
                        tile_surface = platforms_tile_list[int(val)]
                        sprite = StatictTile(tile_size, x, y, tile_surface)

                    if type_ == 'pipes':
                        pipes_tile_list = import_cut_graphics('../pics/pipe3.png')
                        tile_surface = pipes_tile_list[int(val)]
                        sprite = StatictTile(tile_size, x, y, tile_surface)

                    if type_ == 'lucky_blocks':
                        sprite = Lucky_block(tile_size, x, y, '../pics/lucky_blocks/level_1')

                    if type_ == 'funguses_red':
                        sprite = Fungus_red(tile_size, x, y)

                    if type_ == 'coins':
                        sprite = Coin(tile_size, x, y, '../pics/coins/level_1')

                    if type_ == 'trees':
                        sprite = Tree(tile_size, x, y)

                    if type_ == 'castle':
                        castle_tile_list = import_cut_graphics('../pics/castle.png')
                        tile_surface = castle_tile_list[int(val)]
                        sprite = StatictTile(tile_size, x, y, tile_surface)

                    if type_ == 'mountains':
                        mountains_tile_list = import_cut_graphics('../pics/mountain.png')
                        tile_surface = mountains_tile_list[int(val)]
                        sprite = StatictTile(tile_size, x, y, tile_surface)

                    if type_ == 'clouds':
                        sprite = Cloud(tile_size, x, y)

                    if type_ == 'monsters':
                        sprite = Monster(tile_size, x, y)

                    if type_ == 'constraints':
                        sprite = Tile(tile_size, x, y)

                    sprite_group.add(sprite)

        return sprite_group

    def player_setup(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == '0':
                    sprite = Player((x, y), self.display_surface)
                    self.player.add(sprite)

    def camera(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 2
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -2
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 2

    def hor_move_coll(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        coliable_sprites = self.platform_sprites.sprites() + self.pipes_sprites.sprites() + self.lucky_blocks_sprites.sprites()
        for sprite in coliable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vert_move_coll(self):
        player = self.player.sprite
        player.apply_gravity()
        coliable_sprites = (self.platform_sprites.sprites() + self.pipes_sprites.sprites() +
                            self.lucky_blocks_sprites.sprites())

        for sprite in coliable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False

    def kill_fungus(self):
        player = self.player.sprite
        for fung in self.monsters_sprites:
            if fung.rect.colliderect(player.rect) and not player.on_ground:
                if player.direction.y > 0:
                    fung.kill()
                    player.direction.y = 0
                    player.on_ground = True
            elif fung.rect.colliderect(player.rect):
                player.rect.x = player.start_pos[0]

    def get_coins(self):
        player = self.player.sprite
        for coin in self.coins_sprites.sprites():
            if coin.rect.colliderect(player.rect) and not player.on_ground:
                if player.direction.y > 0:
                    self.COUNT_COINS += 1
                    coin.kill()
                    player.on_ground = True
                elif player.direction.y < 0:
                    self.COUNT_COINS += 1
                    coin.kill()

    def get_lucky_blocks(self):
        player = self.player.sprite
        for lucky_bl in self.lucky_blocks_sprites:
            if (lucky_bl.rect.colliderect(player.rect) and not player.on_ground) or (
                    lucky_bl.rect.colliderect(player.rect) and player.on_ground):
                if player.direction.y > 0:
                    self.COUNT_LUCKY_BL += 1
                    lucky_bl.kill()
                    player.on_ground = True
                elif player.direction.y < 0:
                    self.COUNT_LUCKY_BL += 1
                    lucky_bl.kill()

    def collision_reverse(self):
        for monster in self.monsters_sprites.sprites():
            if pygame.sprite.spritecollide(monster, self.constraints_sprites, False):
                monster.reverse_speed()

    def run(self):
        self.platform_sprites.update(self.world_shift)
        self.platform_sprites.draw(self.display_surface)

        self.pipes_sprites.update(self.world_shift)
        self.pipes_sprites.draw(self.display_surface)

        self.trees_sprites.update(self.world_shift)
        self.trees_sprites.draw(self.display_surface)

        self.lucky_blocks_sprites.update(self.world_shift)
        self.lucky_blocks_sprites.draw(self.display_surface)

        self.castle_sprites.update(self.world_shift)
        self.castle_sprites.draw(self.display_surface)

        self.mountains_sprites.update(self.world_shift)
        self.mountains_sprites.draw(self.display_surface)

        self.coins_sprites.update(self.world_shift)
        self.coins_sprites.draw(self.display_surface)

        self.clouds_sprites.update(self.world_shift)
        self.clouds_sprites.draw(self.display_surface)

        self.fungus_red_sprites.update(self.world_shift)
        self.fungus_red_sprites.draw(self.display_surface)

        self.monsters_sprites.update(self.world_shift)
        self.constraints_sprites.update(self.world_shift)
        self.collision_reverse()
        self.kill_fungus()
        self.monsters_sprites.draw(self.display_surface)

        self.camera()

        self.player.update()
        self.hor_move_coll()
        self.vert_move_coll()
        self.player.draw(self.display_surface)
        self.get_coins()
        self.get_lucky_blocks()
