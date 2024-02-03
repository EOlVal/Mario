import pygame
from support import import_folder
import const as c


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surfase):
        super().__init__()
        self.import_mario_skins()
        self.frame_ind = 0
        self.anim_speed = 0.15
        self.image = self.animations['stay'][self.frame_ind]
        self.rect = self.image.get_rect(topleft=pos)
        self.start_pos = pos

        self.boost = False
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 1
        self.gravity = 0.2
        self.jump_speed = -5.5

        self.stat = 'stay'
        self.right_stat = True

        self.on_ground = False

        self.isdeath = False

    def import_mario_skins(self):
        mario_path_1 = '../pics/mario/'
        mario_path_2 = '../pics/mario_2/'

        if c.COUNT_RED_F == 0:
            self.animations = {'stay': [], 'run': [], 'jump': [], 'death': []}

        elif c.COUNT_RED_F > 0:
            self.animations = {'stay_2': [], 'run_2': [], 'jump_2': []}

        for anim in self.animations.keys():
            if c.COUNT_RED_F == 0:
                full_path = mario_path_1 + anim
                self.animations[anim] = import_folder(full_path)
            elif c.COUNT_RED_F:
                full_path = mario_path_2 + anim
                self.animations[anim] = import_folder(full_path)

    def animate(self):
        self.import_mario_skins()
        animation = self.animations[self.stat]
        self.frame_ind += self.anim_speed
        if self.frame_ind >= len(animation):
            self.frame_ind = 0

        image = animation[int(self.frame_ind)]

        if self.right_stat:
            self.image = image
        else:
            flip_image = pygame.transform.flip(image, True, False)
            self.image = flip_image

    def keys_keyboard(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.right_stat = True

        elif keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT]:
            self.direction.x = 1
            self.right_stat = True
            self.boost = True

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.right_stat = False

        elif keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT]:
            self.direction.x = -1
            self.right_stat = False
            self.boost = True

        elif keys[pygame.K_ESCAPE]:
            c.ESC = True

        else:
            self.direction.x = 0

        if (keys[pygame.K_UP] or keys[pygame.K_SPACE]) and self.on_ground:
            c.jump.play()
            self.jump()

    def status(self):
        if self.direction.y < 0 and c.COUNT_RED_F == 0:
            self.stat = 'jump'
        elif self.direction.y < 0 < c.COUNT_RED_F:
            self.stat = 'jump_2'
        else:
            if self.direction.x != 0 and c.COUNT_RED_F == 0:
                self.stat = 'run'
            elif self.direction.x != 0 and c.COUNT_RED_F:
                self.stat = 'run_2'
            else:
                if c.COUNT_RED_F == 0:
                    self.stat = 'stay'
                elif c.COUNT_RED_F:
                    self.stat = 'stay_2'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
        if c.COUNT_RED_F == 0:
            self.stat = 'jump'
        elif c.COUNT_RED_F:
            self.stat = 'jump_2'

    def update(self):
        self.keys_keyboard()
        self.status()
        self.animate()
