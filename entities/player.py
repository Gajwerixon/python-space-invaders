import pygame

from config import *

class Player(pygame.sprite.Sprite):
    """Player class"""
    def __init__(self, groups):
        super().__init__(groups) 
        self.image = pygame.image.load('assets/entities/player/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)

        green = pygame.Surface(self.image.get_size()).convert_alpha()
        green.fill(GREEN)
        self.image.blit(green, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        self.rect = self.image.get_rect(midbottom=(PLAY_AREA.centerx, PLAY_AREA.bottom - 64))
        self.pos = pygame.Vector2(self.rect.center)

        self.direction = pygame.Vector2()
        self.speed = PLAYER_SPEED

    def input(self):
        """Player input"""
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.direction.x = 1
        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

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

    def update(self, dt):
        """Update player"""
        self.input()
        self.movement(dt)
