import pygame

from config import *

class Bullet(pygame.sprite.Sprite):
    """Bullet class"""
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface(BULLET_SIZE)
        self.image.fill('white')
        self.rect = self.image.get_rect(midbottom = pos)

        self.speed = BULLET_SPEED

    def update(self, dt):
        """Update bullet"""
        self.movement(dt)

    def movement(self, dt):
        """Bullet movement"""
        self.rect.y += -1 * self.speed * dt
        if self.rect.top <= PLAY_AREA.top:
            self.kill()