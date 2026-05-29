import pygame
from systems import Timer

class EffectManager:
    """Effect Manager"""
    def __init__(self, group):
        self.group = group

    def spaw_bullet_alien_explosion(self, image, pos, duration):
        """Spawne explosion effect between bullet and alien"""
        Effect(image, pos, duration, self.group)
    
    def spaw_bullet_shield_explosion(self, image, pos, duration):
        """Spawn explosion effect between bullet and shield"""
        Effect(image, pos, duration, self.group)

    def spawn_bullet_miss_explosion(self, image, pos, duration):
        """Spaw explosion effect after bullet miss"""
        Effect(image, pos, duration, self.group, anchor='midtop')

    def spaw_bullet_miss_explosion(self, image, pos, duration):
        Effect(image, pos, duration, self.group, anchor='midtop')

class Effect(pygame.sprite.Sprite):
    """Effect class"""
    def __init__(self, image, pos, duration, groups, anchor="center"):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect()
        setattr(self.rect, anchor, pos)

        self.timer = Timer(duration)
        self.timer.start()

    def update(self, dt):
        """Update explosion"""
        if self.timer.active:
            self.timer.update(dt)
        else:
            self.kill()