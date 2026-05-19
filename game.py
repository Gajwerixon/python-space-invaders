import pygame

from config import *

from level import Level
from hud import HUD

from entities.player import Player
from entities.bullet import Bullet

class Game:
    """Game class"""
    def __init__(self):    
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Space_Invaders')
        self.clock = pygame.time.Clock()
        self.running = True
        self.mode = 'PLAYING'

        # Game variables
        self.lives = 3
        self.credit = 0
        self.score = 0
        self.high_score = 0

        # Groups
        self.player_group = pygame.sprite.Group()
        self.shield_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        
        # Sprites
        self.player = Player(self, self.player_group)

        # Level and HUD
        self.level = Level(self.shield_group)
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
        self.shield_group.update(dt)
        self.bullet_group.update(dt)

    def draw(self):
        """Draw on screen"""
        self.surface.fill('black')
        
        self.player_group.draw(self.surface)
        self.shield_group.draw(self.surface)
        self.bullet_group.draw(self.surface)

        self.hud.draw_hud(self.surface)

        pygame.display.flip()

    def create_bullet(self, pos):
        """Create bullet"""
        if not self.bullet_group:
            Bullet(pos, self.bullet_group)