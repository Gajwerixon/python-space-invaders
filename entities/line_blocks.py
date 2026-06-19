import pygame

from config import LINES

class LineBlocks(pygame.sprite.Sprite):
    """Line Blocks class"""
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.Surface(LINES['size'])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft = pos)

    def damage_line(self):
        """Handle line damage"""
        pass