import pygame
from config import *
from entities.effect import Effect

class Bullet(pygame.sprite.Sprite):
    """Bullet class"""
    def __init__(self, pos, game, groups):
        super().__init__(groups)
        self.image = pygame.Surface(BULLET_SIZE)
        self.image.fill('white')
        self.rect = self.image.get_rect(midbottom = pos)

        self.speed = BULLET_SPEED

        self.game = game

    def update(self, dt):
        """Update bullet"""
        self.movement(dt)

    def movement(self, dt):
        """Bullet movement"""
        self.rect.y += -1 * self.speed * dt
        if self.rect.top <= PLAY_AREA.top:
            current_pos = self.rect.midtop
            self.kill()
            self.game.effect_manager.spaw_bullet_miss_explosion(
                self.game.effects_assets['bullet_miss_fx'],
                current_pos,
                0.25,
            )

