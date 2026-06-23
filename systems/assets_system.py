import pygame

from pathlib import Path
from config import FONT_SIZE, EXPLOSIONS, PLAYER, ALIENS_FORMATION, ALIENS_SHOOTING, UFO, BOTTOM_HUD

class AssetsSystem:
    def __init__(self):
        self.aliens = self.load_alien_assets()
        self.effects = self.load_effects_assets()
        self.player = self.load_player_assets()
        self.font = self.load_font_assets()
        self.font_images = self.load_font_images_assets()
        self.ufo = self.load_ufo_assets()
        self.sounds = self.load_sounds_assets()

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
        return pygame.transform.scale(img, size)

    def load_effects_assets(self):
        effects = {
            'player_bullet_fx': self.load_asset('assets/entities/effect/player/player_bullet_fx.png', 
                                                EXPLOSIONS['player_bullet_miss_size']),
            'player_explosion': [self.load_asset('assets/entities/effect/player/player_explosion_0.png', 
                                                PLAYER['size']),
                                 self.load_asset('assets/entities/effect/player/player_explosion_1.png',
                                                 PLAYER['size'])],
            'alien_bullet_fx': self.load_asset('assets/entities/effect/alien/alien_bullet_fx.png', 
                                               EXPLOSIONS['alien_bullet_miss_size']), 
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
    
    def load_sounds_assets(self):
        return {
            'player': {
                'shoot': self.load_sound('assets/sounds/player_shoot.wav', 0.25),
                'dead': self.load_sound('assets/sounds/player_dead.mp3', 0.25)
            },
            'alien': {
                'movement_1': self.load_sound('assets/sounds/alien_movement_1.wav'),
                'movement_2': self.load_sound('assets/sounds/alien_movement_2.wav'),
                'movement_3': self.load_sound('assets/sounds/alien_movement_3.wav'),
                'movement_4': self.load_sound('assets/sounds/alien_movement_4.wav')
            },
            'ufo': {
                'movement': self.load_sound('assets/sounds/ufo_movement.wav')
            },
        }

    def load_sound(self, path, volume=1.0):
        sound = pygame.mixer.Sound(path)
        sound.set_volume(volume)
        return sound
    
    def load_font_images_assets(self):
        return {
            'top_hud': {
                0: self.load_asset('assets/digit_images/0.png', (15, 21)),
                1: self.load_asset('assets/digit_images/1.png', (15, 21)),
                2: self.load_asset('assets/digit_images/2.png', (15, 21)),
                3: self.load_asset('assets/digit_images/3.png', (15, 21)),
                4: self.load_asset('assets/digit_images/4.png', (15, 21)),
                5: self.load_asset('assets/digit_images/5.png', (15, 21)),
                6: self.load_asset('assets/digit_images/6.png', (15, 21)),
                7: self.load_asset('assets/digit_images/7.png', (15, 21)),
                8: self.load_asset('assets/digit_images/8.png', (15, 21)),
                9: self.load_asset('assets/digit_images/9.png', (15, 21)),
            },
            'bottom_hud': {
                0: self.load_asset('assets/digit_images/0.png', (17, 24)),
                1: self.load_asset('assets/digit_images/1.png', (17, 24)),
                2: self.load_asset('assets/digit_images/2.png', (17, 24)),
                3: self.load_asset('assets/digit_images/3.png', (17, 24)),
                4: self.load_asset('assets/digit_images/4.png', (17, 24)),
                5: self.load_asset('assets/digit_images/5.png', (17, 24)),
                6: self.load_asset('assets/digit_images/6.png', (17, 24)),
                7: self.load_asset('assets/digit_images/7.png', (17, 24)),
                8: self.load_asset('assets/digit_images/8.png', (17, 24)),
                9: self.load_asset('assets/digit_images/9.png', (17, 24)),
            },
        }