import pygame

from config import *

class Shield(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('assets/entities/shield/shield_0.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, SHIELD_SIZE)

        green = pygame.Surface(self.image.get_size()).convert_alpha()
        green.fill(GREEN)
        self.image.blit(green, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        self.rect = self.image.get_rect(topleft = pos)

    def hit(self, pos):
        pass