import pygame
from systems.timer_system import TimerSystem

class Effect(pygame.sprite.Sprite):
    """Effect class"""
    def __init__(self, image, pos, duration, type, groups, anchor="center"):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect()
        setattr(self.rect, anchor, pos)

        self.timer = TimerSystem(duration)
        self.timer.start()

        self.type = type

    def update(self, dt):
        """Update explosion"""
        if self.timer.active:
            self.timer.update(dt)
        else:
            self.kill()