import pygame

from pathlib import Path
from config import *

class AssetsSystem:
    """Assets system class"""
    def __init__(self):
        self.aliens = self.load_alien_assets()
        self.effects = self.load_effects_assets()
        self.player = self.load_player_assets()
        self.font = self.load_font_assets()
        self.ufo = self.load_ufo_assets()

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
    
    def load_asset(self, path, size):
        """Load assets function"""
        img = pygame.image.load(path).convert_alpha()
        img_scale = pygame.transform.scale(img, size)
        return img_scale

    def load_effects_assets(self):
        """Load effects assets"""
        effects = {
            'player_bullet_fx': self.load_asset('assets/entities/effect/player/player_bullet_fx.png', 
                                                MISS_EXPLOSION_FX_SIZE),
            'player_explosion': [self.load_asset('assets/entities/effect/player/player_explosion_0.png', 
                                                PLAYER_SIZE),
                                 self.load_asset('assets/entities/effect/player/player_explosion_1.png',
                                                 PLAYER_SIZE)],
            'alien_bullet_fx': self.load_asset('assets/entities/effect/alien/alien_bullet_fx.png', 
                                               MISS_ALIEN_EXPLOSION_FX_SIZE), 
            'alien_explosion_fx': self.load_asset('assets/entities/effect/alien/alien_explosion_fx.png',
                                                  ALIEN_EXPLOSION_FX_SIZE)
        }
        return effects
    
    def load_player_assets(self):
        """Load player assets"""
        player_assets = {
            'player_img': self.load_asset('assets/entities/player/player.png', PLAYER_SIZE),
            'player_img_hud': self.load_asset('assets/entities/player/player.png', SHIP_IMG_SIZE)
        }
        return player_assets
    
    def load_font_assets(self):
        """Load font assets"""
        return pygame.font.Font('assets/fonts/font.ttf', FONT_SIZE)
    
    def load_ufo_assets(self):
        """Load ufo assets"""
        return self.load_asset('assets/entities/ufo/ufo_img.png', (48, 21))