import pygame
from config import WIDTH, HEIGHT
from systems.assets_system import AssetsSystem
from game.level import Level
from ui.menu import Menu
from ui.hud import HUD
from ui.game_over import GameOver
from ui.advance_table import AdvanceTable
from systems.sounds_system import SoundSystem

class Game:
    """Main game controller handling the state machine, updates, and rendering."""
    def __init__(self):    
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Space_Invaders')
        self.clock = pygame.time.Clock()
        self.running = True

        # Game variables
        self.mode = 'MENU'
        self.num_players = None
        self.credits = 0
        self.high_score = 0

        # Assets and HUD
        self.assets = AssetsSystem()
        self.sound_system = SoundSystem(self.assets.sounds)
        self.hud = HUD(self.assets.player['player_img_hud'], self.assets.font, self.assets.font_images)

        # State Objects
        self.menu = None
        self.advance_table = None
        self.level = None
        self.game_over = None
        self.groups = None

        # Switch to the MENU phase at the beginning
        self.switch_to_menu()

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

            elif self.mode == 'MENU' and self.menu:
                self.menu.handle_events(event)

            elif self.mode == 'ADVANCE_TABLE' and self.advance_table:
                self.advance_table.handle_events(event)

    # --- State Switches ---

    def switch_to_menu(self):
        """Switch to MENU mode"""
        self.level = None
        self.groups = None
        self.advance_table = None
        self.game_over = None
        
        self.menu = Menu(self.assets.font, self.sound_system)
        self.mode = 'MENU'

    def switch_to_advance_table(self):
        """Switch to ADVANCE_TABLE mode"""
        self.num_players = self.menu.get_num_players
        self.menu = None
        
        self.advance_table = AdvanceTable(
            self.assets.font,
            self.assets.aliens, 
            self.assets.ufo['image']
        )
        self.mode = 'ADVANCE_TABLE'

    def switch_to_level(self):
        """Switch to LEVEL mode and initialize game entities"""
        self.advance_table = None
        
        self.groups = self.create_groups()
        self.level = Level(self.groups, self.assets, self.sound_system)
        self.level.create_level()
        self.mode = 'LEVEL'

    def switch_to_game_over(self):
        """Switch to GAME_OVER mode and update high score"""
        if self.level.score_1 > self.high_score:
            self.high_score = self.level.score_1
            
        self.game_over = GameOver(self.assets.font)
        self.mode = 'GAME_OVER'

    # --- Update and Draw functions ---

    def update(self, dt):
        """Update game"""
        if self.mode == 'MENU' and self.menu:
            self.menu.update(dt)
            if self.menu.selection_confirmed:
                self.sound_system.ui_next_phase_play()
                self.switch_to_advance_table()
        
        elif self.mode == 'ADVANCE_TABLE' and self.advance_table:
            self.advance_table.update(dt)
            if self.advance_table.continue_to_game:
                self.sound_system.ui_next_phase_play()
                self.switch_to_level()

        elif self.mode == 'LEVEL' and self.level:
            self.level.update(dt)
            if self.level.phase == 'GAME_OVER':
                self.switch_to_game_over()

        elif self.mode == 'GAME_OVER' and self.game_over:
            self.game_over.update(dt)
            if self.game_over.start_new_game:
                self.switch_to_menu()

    def draw(self):
        """Draw elements on screen"""
        self.surface.fill('black')

        if self.mode == 'MENU' and self.menu:
            self.menu.draw(self.surface)
        
        elif self.mode == 'ADVANCE_TABLE' and self.advance_table:
            self.advance_table.draw(self.surface)
        
        elif self.mode == 'LEVEL' and self.level:
            self.level.draw(self.surface)

        elif self.mode == 'GAME_OVER' and self.game_over:
            self.level.draw(self.surface)
            self.game_over.draw(self.surface)

        # HUD rendering data setup
        score_1 = self.level.score_1 if self.level else 0
        score_2 = self.level.score_2 if self.level else 0
        lives = self.level.lives if self.level else 3

        show_lives = self.mode in ('LEVEL', 'GAME_OVER')

        self.hud.draw_hud(
            score_1, score_2, self.high_score, lives, 
            self.credits, self.surface, show_lives=show_lives)
        
        pygame.display.flip()

    # --- Helper methods ---
    
    def create_groups(self):
        """Initialize and return standard Pygame sprite groups for the level"""
        return {
            'lines': pygame.sprite.Group(),
            'shields': pygame.sprite.Group(),
            'player': pygame.sprite.Group(),
            'aliens': pygame.sprite.Group(),
            'player_bullets': pygame.sprite.Group(),
            'alien_bullets': pygame.sprite.Group(),
            'effects': pygame.sprite.Group(),
            'ufo': pygame.sprite.Group()
        }