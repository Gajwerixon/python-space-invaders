import pygame
from systems import Timer

class Effect(pygame.sprite.Sprite):
    """Effect class"""
    def __init__(self, image, type, pos, duration, groups):
        super().__init__(groups)
        self.image = image
        if type == 'bullet':
            self.rect = self.image.get_rect(midtop = pos)
        else:
            self.rect = self.image.get_rect(center = pos)

        self.bullet_miss_fx = Timer(duration)
        self.bullet_miss_fx.start()

    def update(self, dt):
        """Update explosion"""
        if self.bullet_miss_fx.active:
            self.bullet_miss_fx.update(dt)
        else:
            self.kill()