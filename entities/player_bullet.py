import pygame
from config import PLAYER_BULLETS

class PlayerBullet(pygame.sprite.Sprite):
    """Player Bullet class"""
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface(PLAYER_BULLETS['size'])
        self.image.fill('white')
        self.rect = self.image.get_rect(midbottom = pos)
        self.pos = pygame.Vector2(self.rect.center)

    def update(self, dt):
        """Update PlayerBullet"""
        self.movement(dt)

    def movement(self, dt):
        """PlayerBullet movement"""
        self.pos.y += -1 * PLAYER_BULLETS['speed'] * dt
        self.rect.center = self.pos