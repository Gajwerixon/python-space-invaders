import pygame

from config import *

from entities.player import Player

from systems.aliens_systems import AliensSystem
from systems.assets_system import AssetsSystem
from systems.effect_system import EffectSystem
from systems.collision_system import CollisionSystem

from ui.menu import Menu
from ui.hud import HUD
from ui.advance_table import AdvanceTable
from game.level import Level

class Game:
    """Game class"""
    def __init__(self):    
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Space_Invaders')
        self.clock = pygame.time.Clock()
        self.running = True

        self.mode = 'ADVANCE_TABLE'
        self.lives = 3
        self.credit = 0
        self.score_1 = 0
        self.score_2 = 0
        self.high_score = 0

        self.assets = AssetsSystem()

        self.player_group = pygame.sprite.Group()
        self.shield_blocks_group = pygame.sprite.Group()
        self.player_bullets_group = pygame.sprite.Group()
        self.alien_bullets_group = pygame.sprite.Group()
        self.effects_group = pygame.sprite.Group()
        self.aliens_group = pygame.sprite.Group()
        
        self.player = Player(self.assets.player['player_img'], self.player_bullets_group, self.player_group)

        self.aliens_system = AliensSystem(self.assets.aliens, self.alien_bullets_group, self.aliens_group)
        self.effect_system = EffectSystem(self.assets.effects, self.effects_group)
        self.collision_system = CollisionSystem(self.player_group,
                                                self.shield_blocks_group,
                                                self.player_bullets_group,
                                                self.alien_bullets_group,
                                                self.aliens_group,
                                                self.effect_system)

        self.hud = HUD(self.assets.player['player_img_hud'], self.assets.font)
        self.menu = Menu(self.assets.font)
        self.advance_table = AdvanceTable(self.assets.font, self.assets.aliens, self.assets.ufo)
        self.level = Level(self.shield_blocks_group)

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
            elif self.mode == 'MENU':
                self.menu.handle_events(event)
            elif self.mode == 'ADVANCE_TABLE':
                self.advance_table.handle_events(event)

    def update(self, dt):
        """Update game"""
        if self.mode == 'MENU':
            self.update_menu(dt)
        
        if self.mode == 'ADVANCE_TABLE':
            self.update_advance_table(dt)

        if self.mode == 'PLAYING':
            self.update_playing(dt)

    def draw(self):
        """Draw elements on screen"""
        self.surface.fill('black')

        if self.mode == 'MENU':
            self.menu.draw(self.surface)
        
        elif self.mode == 'ADVANCE_TABLE':
            self.advance_table.draw(self.surface)
        
        elif self.mode == 'PLAYING':
            self.draw_playing()

        self.hud.draw_hud(self.score_1, self.score_2, self.high_score, 
                        self.lives, self.credit, self.surface)

        pygame.display.flip()

    def update_menu(self, dt):
        """Update MENU mode"""
        self.menu.update(dt)
        if self.menu.selection_confirmed:
            self.menu.selection_confirmed = False
            self.num_players = self.menu.get_num_players
            self.mode = 'ADVANCE_TABLE'

    def update_advance_table(self, dt):
        """Update ADVANCE_TABLE mode"""
        self.advance_table.update(dt)
        if self.advance_table.start_game:
            self.advance_table.start_game = False
            self.mode = 'PLAYING'

    def update_playing(self, dt):
        """Update PLAYING mode"""
        self.player_group.update(dt)
        self.shield_blocks_group.update(dt)
        self.alien_bullets_group.update(dt)
        self.player_bullets_group.update(dt)
        self.effects_group.update(dt)

        self.aliens_system.update(dt)
        self.collision_system.update()

    def draw_playing(self):
        """Draw elements on screen at PLAYING mode"""
        self.alien_bullets_group.draw(self.surface)
        self.player_bullets_group.draw(self.surface)
        self.shield_blocks_group.draw(self.surface)
        self.player_group.draw(self.surface)
        self.aliens_group.draw(self.surface)
        self.effects_group.draw(self.surface)