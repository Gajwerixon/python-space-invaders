import pygame

from pathlib import Path
from config import *
from level import Level
from hud import HUD
from entities.player import Player
from entities.bullet import Bullet
from entities.effect import EffectManager
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
        self.aliens_assets, self.effects_assets = self.load_assets()

        # Groups
        self.player_group = pygame.sprite.Group()
        self.shield_blocks_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.effect_group = pygame.sprite.Group()
        self.alien_group = pygame.sprite.Group()
        
        # Sprites
        self.player = Player(self, self.player_group)
        self.formation = AlienFormation(self.aliens_assets, self.alien_group)

        # Level, HUD and Effect
        self.level = Level(self.shield_blocks_group)
        self.hud = HUD(self)
        self.effect_manager = EffectManager(self.effect_group)

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
        self.bullet_group.update(dt)
        self.effect_group.update(dt)

        self.bullet_alien_collision()
        self.bullet_shield_collision()

    def draw(self):
        """Draw on screen"""
        self.surface.fill('black')
        
        self.player_group.draw(self.surface)
        self.shield_blocks_group.draw(self.surface)
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
        collision = pygame.sprite.groupcollide(
            self.bullet_group, 
            self.alien_group, 
            True, 
            True
        )

        for _, aliens in collision.items():
            self.effect_manager.spaw_bullet_alien_explosion(
                self.effects_assets['alien_explosion_fx'],
                aliens[0].rect.center,
                0.25
            )      
            
    def bullet_shield_collision(self):
        """Bullet and shield collision"""
        collision = pygame.sprite.groupcollide(self.bullet_group, self.shield_blocks_group, True, True)
        for bullet, shields in collision.items():
            shields[0].damage_shield()
            self.effect_manager.spaw_bullet_shield_explosion(
                self.effects_assets['bullet_miss_fx'],
                bullet.rect.midtop,
                0.25
            ) 

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