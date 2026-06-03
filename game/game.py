import pygame

from config import *

from entities.player import Player

from systems.aliens_systems import AliensSystem
from systems.assets_system import AssetsSystem
from systems.effect_system import EffectSystem
from systems.collision_system import CollisionSystem

from game.level import Level
from ui.hud import HUD

class Game:
    """Game class"""
    def __init__(self):    
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Space_Invaders')
        self.clock = pygame.time.Clock()
        self.running = True

        # Game variables
        self.mode = 'PLAYING'
        self.lives = 3
        self.credit = 0
        self.score = 0
        self.high_score = 0

        # Assets
        self.assets = AssetsSystem()
        self.aliens_assets = self.assets.aliens
        self.effects_assets = self.assets.effects

        # Groups
        self.player_group = pygame.sprite.Group()
        self.shield_blocks_group = pygame.sprite.Group()
        self.player_bullets_group = pygame.sprite.Group()
        self.alien_bullets_group = pygame.sprite.Group()
        self.effects_group = pygame.sprite.Group()
        self.aliens_group = pygame.sprite.Group()
        
        # Sprites
        self.player = Player(self.player_bullets_group, self.player_group)

        # Systems
        self.aliens_system = AliensSystem(self.aliens_assets, self.alien_bullets_group, self.aliens_group)
        self.effect_system = EffectSystem(self.effects_assets, self.effects_group)
        self.collision_system = CollisionSystem(self.player_group,
                                                self.shield_blocks_group,
                                                self.player_bullets_group,
                                                self.alien_bullets_group,
                                                self.aliens_group,
                                                self.effect_system)

        # Level and HUD
        self.level = Level(self.shield_blocks_group)
        self.hud = HUD(self)

    def run(self):
        """Main game loop"""
        while self.running:
            dt = self.clock.tick(60) / 1000
            self.handle_events()
            self.update(dt)
            self.draw()

    def handle_events(self):
        """Handle events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt):
        """Update game"""
        self.player_group.update(dt)
        self.shield_blocks_group.update(dt)
        self.alien_bullets_group.update(dt)
        self.player_bullets_group.update(dt)
        self.effects_group.update(dt)

        self.aliens_system.update(dt)
        self.collision_system.update()

    def draw(self):
        """Draw on screen"""
        self.surface.fill('black')
        
        self.alien_bullets_group.draw(self.surface)
        self.player_bullets_group.draw(self.surface)
        self.shield_blocks_group.draw(self.surface)
        self.player_group.draw(self.surface)
        self.aliens_group.draw(self.surface)
        self.effects_group.draw(self.surface)

        self.hud.draw_hud(self.surface)

        pygame.display.flip()                                           