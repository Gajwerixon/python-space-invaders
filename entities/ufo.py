import pygame

from config import *

class Ufo(pygame.sprite.Sprite):
    """Ufo class"""
    def __init__(self, pos, image, score, group):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.score = score
        