import pygame

from config import *
from systems import Timer

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
            Effect(
                self.game.effects_assets['bullet_miss_fx'], 
                current_pos, 
                self.game.effect_group
            )

class Effect(pygame.sprite.Sprite):
    """Effect class"""
    def __init__(self, image, pos, groups):
        super().__init__(groups)
        self.image = image
        self.image = pygame.transform.scale(self.image, EXPLOSION_SIZE)
        self.rect = self.image.get_rect(midtop = pos)

        self.bullet_miss_fx = Timer(0.25)
        self.bullet_miss_fx.start()

    def update(self, dt):
        """Update explosion"""
        if self.bullet_miss_fx.active:
            self.bullet_miss_fx.update(dt)
        else:
            self.kill()

