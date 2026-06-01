import pygame

from config import *
from systems import Timer

class AlienFormation:
    """Alien formation"""
    def __init__(self, assets, group):
        self.assets = assets
        self.alien_group = group

        # Create formation
        self.start_pos = (64, PLAY_AREA.bottom - 400)
        self.formation_list = []
        self.create_formation()

        # State
        self.state = 'move_horizontal'

        # Movement
        self.descent_step_x = DESCENT_STEP_X
        self.direction = pygame.Vector2(1, 0)
        self.alien_timer = Timer(ALIEN_TIMER)

        # Current variables
        self.current_alien = 0
        self.animation_index = 1
        self.cycle_completed = False


    def update(self, dt):
        """Update alien formation"""
        self.alien_timer.update(dt)
        self.update_formation()
        if self.cycle_completed:
            self.toggle_animation_frame()
            self.cycle_completed = False

    def draw(self, surface):
        """Draw alien formation"""
        for alien in self.alien_group:
            surface.blit(alien.image, alien.rect.topleft)

    def update_formation(self):
        """Update formation"""
        alien = self.get_current_alien()
        if not alien.alive():
            self.current_alien = self.get_alive_index()
        else:
            self.movement(alien)

    def get_current_alien(self):
        """Get current alien"""
        return self.formation_list[self.current_alien]

    def get_alive_index(self):
        """Get next alive index of alien in formation"""
        start = self.current_alien
        index = start

        while True:

            if self.formation_list[index].alive():
                return index

            index += 1

            if index >= len(self.formation_list):
                index = 0

            if index == start:
                return None

    def create_formation(self):
        """Create alien formation"""
        for alien_col, alien_type in enumerate(ALIENS_SETUP):
            for alien_row in range(NUM_ALIENS):
                self.formation_list.append(Alien(
                    (self.start_pos[0] + (alien_row * (ALIEN_STEP + ALIEN_SIZE[0])), 
                    self.start_pos[1] - (alien_col * (ALIEN_STEP + ALIEN_SIZE[1]))),
                    self.assets[alien_type]['images'],
                    self.assets[alien_type]['bullets'],
                    ALIEN_SCORE[alien_type],
                    self.alien_group
                ))

class Alien(pygame.sprite.Sprite):
    """Alien class"""
    def __init__(self, pos, images, bullets, score, alien_group):
        super().__init__(alien_group)
        self.images = images
        self.image = images[0]
        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.Vector2(self.rect.center)

        self.bullets = bullets
        self.score = score
        
        # Flags
        self.double_step = False