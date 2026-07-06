import pygame

from config import PLAY_AREA, PLAYER, WIDTH
from entities.player_bullet import PlayerBullet
from systems.sounds_system import SoundSystem

class Player(pygame.sprite.Sprite):
    """Player class"""
    def __init__(self, image, player_bullets_group, groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(
            midbottom=(
                PLAYER['start_x'], 
                PLAY_AREA.bottom - PLAYER['start_y_offset'])
        )
        self.pos = pygame.Vector2(self.rect.center)

        self.direction = pygame.Vector2()
        self.speed = PLAYER['speed']
        self.space_relase = True

        self.bullets = player_bullets_group

        self.events = []

    def update(self, dt):
        """Update player"""
        self.input()
        self.movement(dt)

    def movement(self, dt):
        """Player movement"""
        if self.direction.x != 0:
            self.pos.x += self.direction.x * self.speed * dt

            half_width = self.rect.width / 2
            if self.pos.x > WIDTH - half_width:
                self.pos.x = WIDTH - half_width

            if self.pos.x < 0 + half_width:
                self.pos.x = 0 + half_width

            self.rect.centerx = self.pos.x
            self.rect.centery = self.pos.y

    def input(self):
        """Player input"""
        key = pygame.key.get_pressed()
        pygame.key.set_repeat(200, 50)
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.direction.x = 1
        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            self.direction.x = -1
        elif not (key[pygame.K_LEFT] or key[pygame.K_a] or key[pygame.K_RIGHT] or key[pygame.K_d]):
            self.direction.x = 0

        if key[pygame.K_SPACE]:
            if len(self.bullets) <= 0 and self.space_relase:
                PlayerBullet(self.rect.midtop, self.bullets)
                self.events.append('PLAYER_SHOOT')
                self.space_relase = False
        else:
            self.space_relase = True