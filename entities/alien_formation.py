import pygame

from config import *
from systems import Timer

class AlienFormation:
    """Alien formation"""
    def __init__(self, assets, group):
        self.assets = assets
        self.alien_group = group

        self.start_pos = (64, PLAY_AREA.bottom - 400)
        self.formation_list = []
        self.create_formation()

        self.direction = pygame.Vector2(1, 0)
        self.alien_timer = Timer(ALIEN_TIMER)

        self.state = 'move_horizontal'
        self.current_alien = 0
        self.animation_index = 1

    def update(self, dt):
        """Update alien formation"""
        self.alien_timer.update(dt)
        self.update_formation()

    def draw(self, surface):
        """Draw alien formation"""
        for alien in self.alien_group:
            surface.blit(alien.image, alien.rect.topleft)

    def update_formation(self):
        """Update formation"""
        if self.alien_timer.active:
            return
        
        alien = self.get_current_alien()

        if not alien.alive():
            self.current_alien = self.find_next_alive_index()
            return
        
        if self.state == 'move_horizontal':
            self.move_horizontal(alien)
        else:
            self.move_vertical(alien)

        self.update_alien_visuals(alien)

        wall_collision = self.check_wall_collision()
        self.advance_cycle(wall_collision)
        self.alien_timer.start()

    def move_horizontal(self, alien):
        """Move alien horizontal"""
        alien.pos.x += self.direction.x * HORIZONTAL_STEP

    def move_vertical(self, alien):
        """Move current alien vertical"""
        alien.pos.x += self.direction.x * (HORIZONTAL_STEP * 2)
        alien.pos.y += VERTICAL_STEP

    def check_wall_collision(self):
        """Check wall collision"""
        for alien in self.formation_list:
            if alien.alive():
                if alien.rect.right >= PLAY_AREA.right - FORMATION_MARGIN or alien.rect.left <= FORMATION_MARGIN:
                    return True
        return False

    def advance_cycle(self, wall_collision):
        """Advance cycle"""
        self.current_alien += 1

        if self.current_alien >= len(self.formation_list):
            self.current_alien = 0
            self.animation_index = 1 - self.animation_index

            if wall_collision:
                self.state = 'move_vertical'
                self.direction *= -1
            else:
                self.state = 'move_horizontal'

    def get_current_alien(self):
        """Get current alien"""
        return self.formation_list[self.current_alien]

    def find_next_alive_index(self):
        """Get next alive index of alien in formation"""
        start = self.current_alien
        index = start

        while True:
            index += 1

            if index >= len(self.formation_list):
                index = 0

            if self.formation_list[index].alive():
                return index

            if index == start:
                return None

    def update_alien_visuals(self, alien):
        """Update alien position and change alien image"""
        alien.rect.center = alien.pos
        alien.image = alien.images[self.animation_index]

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