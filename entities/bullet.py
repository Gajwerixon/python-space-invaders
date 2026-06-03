import pygame
from config import *

class Bullet(pygame.sprite.Sprite):
    """Bullet class"""
    def __init__(self, pos, direction_y, groups):
        super().__init__(groups)
        self.image = pygame.Surface(BULLET_SIZE)
        self.image.fill('white')
        self.rect = self.image.get_rect(midbottom = pos)
        self.pos = pygame.Vector2(self.rect.center)

        self.direction_y = direction_y 
        self.speed = BULLET_SPEED

    def update(self, dt):
        """Update bullet"""
        self.movement(dt)

    def movement(self, dt):
        """Bullet movement"""
        self.pos.y += self.direction_y * self.speed * dt
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y