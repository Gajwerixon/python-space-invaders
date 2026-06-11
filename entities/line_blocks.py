import pygame

from config import *

class LineBlocks(pygame.sprite.Sprite):
    """Line Blocks class"""
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.Surface(LINE_SIZE)
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft = pos)