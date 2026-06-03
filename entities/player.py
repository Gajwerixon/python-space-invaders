import pygame

from config import *

class Player(pygame.sprite.Sprite):
    """Player class"""
    def __init__(self, game, groups):
        super().__init__(groups)
        self.game = game

        self.image = pygame.image.load('assets/entities/player/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
        self.rect = self.image.get_rect(midbottom=(PLAY_AREA.centerx, PLAY_AREA.bottom - 60))
        self.pos = pygame.Vector2(self.rect.center)

        self.direction = pygame.Vector2()
        self.speed = PLAYER_SPEED
    
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
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.direction.x = 1
        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            self.direction.x = -1
        elif not (key[pygame.K_LEFT] or key[pygame.K_a] or key[pygame.K_RIGHT] or key[pygame.K_d]):
            self.direction.x = 0

        if key[pygame.K_SPACE]:
            self.game.create_player_bullet(self.rect.midtop)