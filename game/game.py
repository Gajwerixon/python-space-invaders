import pygame

from config import *

from systems.assets_system import AssetsSystem

from game.level import Level

from ui.menu import Menu
from ui.hud import HUD
from ui.game_over import GameOver
from ui.advance_table import AdvanceTable

class Game:
    """Game class"""
    def __init__(self):    
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Space_Invaders')
        self.clock = pygame.time.Clock()
        self.running = True

        self.mode = 'MENU'
        self.num_players = None
        self.credit = 0
        self.high_score = 0

        self.assets = AssetsSystem()

        self.groups = {
            'lines': pygame.sprite.Group(),
            'shields': pygame.sprite.Group(),
            'player': pygame.sprite.Group(),
            'aliens': pygame.sprite.Group(),
            'player_bullets': pygame.sprite.Group(),
            'alien_bullets': pygame.sprite.Group(),
            'effects': pygame.sprite.Group(),
            'ufo': pygame.sprite.Group()
        }

        self.level = Level(self.groups, self.assets)

        self.hud = HUD(self.assets.player['player_img_hud'], self.assets.font)
        self.game_over = GameOver(self.assets.font)
        self.menu = Menu(self.assets.font)
        self.advance_table = AdvanceTable(self.assets.font, self.assets.aliens, self.assets.ufo['image'])

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            self.handle_events()
            self.update(dt)
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif self.mode == 'MENU':
                self.menu.handle_events(event)

    def update(self, dt):
        if self.mode == 'MENU':
            self.update_menu(dt)
        
        elif self.mode == 'ADVANCE_TABLE':
            self.update_advance_table(dt)

        elif self.mode == 'LEVEL':
            self.update_level(dt)

        elif self.mode == 'GAME_OVER':
            self.update_game_over(dt)

    def draw(self):
        self.surface.fill('black')

        if self.mode == 'MENU':
            self.menu.draw(self.surface)
        
        elif self.mode == 'ADVANCE_TABLE':
            self.advance_table.draw(self.surface)
        
        elif self.mode == 'LEVEL':
            self.level.draw(self.surface)

        elif self.mode == 'GAME_OVER':
            self.level.draw(self.surface)
            self.game_over.draw(self.surface)

        self.hud.draw_hud(self.level.score_1, self.level.score_2, self.high_score, 
                        self.level.lives, self.credit, self.surface)
        
        pygame.display.flip()

    def update_menu(self, dt):
        """Update MENU mode"""
        self.menu.update(dt)
        if self.menu.selection_confirmed:
            self.num_players = self.menu.get_num_players
            self.mode = 'ADVANCE_TABLE'

    def update_advance_table(self, dt):
        self.advance_table.update(dt)
        if self.advance_table.continue_to_game:
            self.level.initialize_level()
            self.mode = 'LEVEL'

    def update_level(self, dt):
        self.level.update(dt)
        if self.level.phase == 'GAME_OVER':
            self.mode = 'GAME_OVER'

    def update_game_over(self, dt):
        self.game_over.update(dt)
        if self.game_over.start_new_game:
            self.reset_game()

    def reset_game(self):
        self.num_players = None
        self.credit = 0

        self.groups = {
            'lines': pygame.sprite.Group(),
            'shields': pygame.sprite.Group(),
            'player': pygame.sprite.Group(),
            'aliens': pygame.sprite.Group(),
            'player_bullets': pygame.sprite.Group(),
            'alien_bullets': pygame.sprite.Group(),
            'effects': pygame.sprite.Group(),
            'ufo': pygame.sprite.Group()
        }

        self.menu = Menu(self.assets.font)
        self.advance_table = AdvanceTable(self.assets.font, self.assets.aliens, self.assets.ufo)
        self.level = Level(self.groups, self.assets)
        self.game_over = GameOver(self.assets.font)

        self.mode = 'MENU'