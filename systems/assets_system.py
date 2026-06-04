import pygame

from pathlib import Path
from config import *

class AssetsSystem:
    """Assets system class"""
    def __init__(self):
        self.aliens = self.load_alien_assets()
        self.effects = self.load_effects_assets()

    def load_alien_assets(self):
        """Load alien assets"""
        aliens_base_path = Path('assets/entities/aliens/')
        aliens = {}
        for alien in aliens_base_path.iterdir():
            aliens[alien.name] = {}
            for folder in alien.iterdir():
                aliens[alien.name][folder.name] = []              
                for img in folder.iterdir():
                    no_bg_img = pygame.image.load(img).convert()
                    no_bg_img.set_colorkey((0, 0, 0))
                    if folder.name == 'bullets': 
                        ready_img = pygame.transform.scale(no_bg_img, BULLET_SIZE)
                    else: 
                        ready_img = pygame.transform.scale(no_bg_img, ALIEN_SIZE)

                    aliens[alien.name][folder.name].append(ready_img)                    
        return aliens

    def load_effects_assets(self):
        """Load effects assets"""
        effects = {
            'player_bullet_fx': pygame.transform.scale(
                pygame.image.load('assets/entities/effect/player/player_bullet_fx.png'), 
                MISS_EXPLOSION_FX_SIZE).convert_alpha(),
            'player_explosion': [pygame.transform.scale(
                pygame.image.load('assets/entities/effect/player/player_explosion_0.png'), 
                PLAYER_SIZE).convert_alpha(), pygame.transform.scale(
                pygame.image.load('assets/entities/effect/player/player_explosion_1.png'), 
                PLAYER_SIZE).convert_alpha()],
            'alien_bullet_fx': pygame.transform.scale(
                pygame.image.load('assets/entities/effect/alien/alien_bullet_fx.png'), 
                MISS_ALIEN_EXPLOSION_FX_SIZE).convert_alpha(), 
            'alien_explosion_fx': pygame.transform.scale(
                pygame.image.load('assets/entities/effect/alien/alien_explosion_fx.png'), 
                ALIEN_EXPLOSION_FX_SIZE).convert_alpha(),
        }
        return effects