import pygame

from config import *

class Line:
    """Line class manager"""
    def __init__(self):
        ...


class LineBlocks(pygame.sprite.Sprite):
    """Line Blocks class"""
    def __init__(self, groups):
        super().__init__(groups)
        self.line_image = pygame.Surface((WIDTH, LINE_WIDTH))
        self.line_image.fill((255, 255, 255))
        self.line_rect= self.line_image.get_rect(topleft = (0, HUD_BOTTOM_Y))

