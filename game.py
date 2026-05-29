import pygame

from pathlib import Path
from config import *
from level import Level
from hud import HUD
from entities.player import Player
from entities.bullet import Bullet
from entities.effect import Effect
from entities.alien_formation import AlienFormation

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

        # Assets
        self.aliens, self.effects = self.load_assets()

        # Groups
        self.player_group = pygame.sprite.Group()
        self.shield_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.effect_group = pygame.sprite.Group()
        self.alien_group = pygame.sprite.Group()
        
        # Sprites
        self.player = Player(self, self.player_group)
        self.formation = AlienFormation(self.aliens, self.alien_group)

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
        self.effect_group.update(dt)
        self.formation.update(dt)

        self.bullet_alien_collision()

    def draw(self):
        """Draw on screen"""
        self.surface.fill('black')
        
        self.player_group.draw(self.surface)
        self.shield_group.draw(self.surface)
        self.bullet_group.draw(self.surface)
        self.effect_group.draw(self.surface)
        self.formation.draw(self.surface)

        self.hud.draw_hud(self.surface)

        pygame.display.flip()

    def create_bullet(self, pos):
        """Create bullet"""
        if not self.bullet_group:
            Bullet(pos, self, self.bullet_group)

    def bullet_alien_collision(self):
        """Bullet and alien collision"""
        collision = pygame.sprite.groupcollide(self.bullet_group, self.alien_group, True, False)
        if collision:
            for alien in collision.values():
                Effect(self.effects['alien_explosion_fx'], 'explosion', alien[0].rect.center, 0.25, self.effect_group)
                for a in alien:
                    a.kill()
                break          
            
    def load_assets(self):
        """Load assets"""
        aliens_base_path = Path('assets/entities/aliens/')
        aliens = {}
        for alien in aliens_base_path.iterdir():
            aliens[alien.name] = {}
            for folder in alien.iterdir():
                aliens[alien.name][folder.name] = []              
                for img in folder.iterdir():
                    aliens[alien.name][folder.name].append(pygame.transform.scale(
                        pygame.image.load(img), ALIEN_SIZE))

        effects = {
            'bullet_miss_fx': pygame.transform.scale(
                pygame.image.load('assets/entities/effect/bullet_miss_fx.png'), 
                MISS_EXPLOSION_FX_SIZE),
            'alien_explosion_fx': pygame.transform.scale(
                pygame.image.load('assets/entities/effect/alien_explosion_fx.png'), 
                ALIEN_EXPLOSION_FX_SIZE),
        }
                    
        return aliens, effects                                                  