import pygame

from pathlib import Path
from config import FONT_SIZE, EXPLOSIONS, PLAYER, ALIENS_FORMATION, ALIENS_SHOOTING, UFO, BOTTOM_HUD

class AssetsSystem:
    def __init__(self):
        self.aliens = self.load_alien_assets()
        self.effects = self.load_effects_assets()
        self.player = self.load_player_assets()
        self.font = self.load_font_assets()
        self.ufo = self.load_ufo_assets()

    def load_alien_assets(self):
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
                        ready_img = pygame.transform.scale(no_bg_img, ALIENS_SHOOTING['size'])
                    else: 
                        ready_img = pygame.transform.scale(no_bg_img, ALIENS_FORMATION['size'])

                    aliens[alien.name][folder.name].append(ready_img)                    
        return aliens
    
    def load_asset(self, path, size):
        img = pygame.image.load(path).convert_alpha()
        img_scale = pygame.transform.scale(img, size)
        return img_scale

    def load_effects_assets(self):
        effects = {
            'player_bullet_fx': self.load_asset('assets/entities/effect/player/player_bullet_fx.png', 
                                                EXPLOSIONS['alien_bullet_miss_size']),
            'player_explosion': [self.load_asset('assets/entities/effect/player/player_explosion_0.png', 
                                                PLAYER['size']),
                                 self.load_asset('assets/entities/effect/player/player_explosion_1.png',
                                                 PLAYER['size'])],
            'alien_bullet_fx': self.load_asset('assets/entities/effect/alien/alien_bullet_fx.png', 
                                               EXPLOSIONS['player_bullet_miss_size']), 
            'alien_explosion_fx': self.load_asset('assets/entities/effect/alien/alien_explosion_fx.png',
                                                  EXPLOSIONS['alien_size']),
            'ufo_dead': self.load_asset('assets/entities/effect/ufo/ufo_dead.png', UFO['dead_size'])
        }
        return effects
    
    def load_player_assets(self):
        player_assets = {
            'player_img': self.load_asset('assets/entities/player/player.png', PLAYER['size']),
            'player_img_hud': self.load_asset('assets/entities/player/player.png', BOTTOM_HUD['ship_size'])
        }
        return player_assets
    
    def load_font_assets(self):
        return pygame.font.Font('assets/fonts/font.ttf', FONT_SIZE)
    
    def load_ufo_assets(self):
        ufo_assets = {
            'image': self.load_asset('assets/entities/ufo/ufo_img.png', UFO['size']),
        }
        return ufo_assets