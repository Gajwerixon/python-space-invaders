import pygame

from pathlib import Path
from config import FONT_SIZE, EXPLOSIONS, PLAYER, ALIENS_FORMATION, ALIENS_SHOOTING, UFO, BOTTOM_HUD

class AssetsSystem:
    def __init__(self):
        self.aliens = self.load_aliens_assets()
        self.effects = self.load_effects_assets()
        self.player = self.load_player_assets()
        self.ufo = self.load_ufo_assets()

        self.sounds = self.load_sounds_assets()

        self.font = self.load_font_assets()
        self.font_images = self.load_font_images_assets()

    def load_aliens_assets(self):
        """Load aliens assets"""
        aliens_base_path = Path('assets/entities/aliens/')
        aliens = {}
        
        for alien_folder in sorted(aliens_base_path.iterdir()):
            if not alien_folder.is_dir(): 
                continue
                
            aliens[alien_folder.name] = {}
            for folder in sorted(alien_folder.iterdir()):
                if not folder.is_dir(): 
                    continue
                
                aliens[alien_folder.name][folder.name] = []
                
                size = ALIENS_SHOOTING['size'] if folder.name == 'bullets' else ALIENS_FORMATION['size']
                
                for img_path in sorted(folder.iterdir()):
                    if img_path.suffix in ('.png', '.jpg', '.jpeg'):
                        ready_img = self.load_asset(img_path, size)
                        aliens[alien_folder.name][folder.name].append(ready_img)
                        
        return aliens
    
    def load_effects_assets(self):
        return {
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
    
    def load_player_assets(self):
        """Load player assets"""
        return {
            'player_img': self.load_asset('assets/entities/player/player.png', PLAYER['size']),
            'player_img_hud': self.load_asset('assets/entities/player/player.png', BOTTOM_HUD['ship_size'])
        }
    
    def load_ufo_assets(self):
        """Load ufo assets"""
        return {
            'image': self.load_asset('assets/entities/ufo/ufo_img.png', UFO['size']),
        }
    
    def load_sounds_assets(self):
        """Load sound assets"""
        return {
            'player': {
                'shoot': self.load_sound('assets/sounds/player_shoot.wav'),
                'dead': self.load_sound('assets/sounds/player_dead.mp3')
            },
            'alien': {
                'movement':[
                    self.load_sound('assets/sounds/alien_movement_1.wav'),
                    self.load_sound('assets/sounds/alien_movement_2.wav'),
                    self.load_sound('assets/sounds/alien_movement_3.wav'),
                    self.load_sound('assets/sounds/alien_movement_4.wav'),
                ],
                'dead': self.load_sound('assets/sounds/alien_dead.wav', 0.1)
            },
            'ufo': {
                'movement': self.load_sound('assets/sounds/ufo_movement.wav')
            },
            'ui': {
                'next_phase': self.load_sound('assets/sounds/next_phase_sound.mp3'),
                'switch_option': self.load_sound('assets/sounds/switch_option_sound.mp3')
            },
        }

    def load_font_assets(self):
        return pygame.font.Font('assets/fonts/font.ttf', FONT_SIZE)
    
    def load_font_images_assets(self):
        """Load font images assets"""
        return {
            'top_hud': {i: self.load_asset(f'assets/digit_images/{i}.png', (15, 21)) for i in range(10)},
            'bottom_hud': {i: self.load_asset(f'assets/digit_images/{i}.png', (17, 24)) for i in range(10)}
        }
    
    def load_asset(self, path, size):
        """Load image asset"""
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(img, size)
    
    def load_sound(self, path, volume=0.2):
        """Load sound asset"""
        sound = pygame.mixer.Sound(path)
        sound.set_volume(volume)
        return sound