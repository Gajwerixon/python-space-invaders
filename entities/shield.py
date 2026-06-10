import pygame

from config import *
from random import randrange

class ShieldBlocks(pygame.sprite.Sprite):
    """Shield Blocks class"""
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.shield_blocks_group = groups
        self.image = pygame.Surface(((SHIELD_BLOCK_SIZE)))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft = pos)

    def damage_shield(self):
        """Bullet hit shield block"""
        explosion_x, explosion_y  = self.rect.center
        
        for shield in self.shield_blocks_group:
            if self.is_within_explosion_radius(shield, explosion_x, explosion_y):
                if self.is_direct_hit(explosion_x, shield.rect.centerx):
                    if randrange(0, 9) < DIRECTION_DESTROY_CHANCE:
                        shield.kill()
                else:
                    if randrange(0, 9) < EDGE_DESTROY_CHANCE:
                        shield.kill()

    def is_within_explosion_radius(self, shield, explosion_x, explosion_y):
        """Check if shield is in explosion radius"""
        dx = shield.rect.centerx - explosion_x
        dy = shield.rect.centery - explosion_y
        distance = dx*dx + dy*dy

        return distance < EXPLOSION_RADIUS
    
    def is_direct_hit(self, explosion_x, shield_x):
        """
        Check if the shield is the same (or one block on the left)
        direction as a explosion
        """
        if explosion_x == shield_x or explosion_x == shield_x - SHIELD_BLOCK_SIZE[0]:
            return True