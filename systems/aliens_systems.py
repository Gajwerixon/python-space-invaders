import pygame

from config import *
from random import choice

from entities.alien import Alien
from entities.alien_bullet import AlienBullet

from systems.timer_system import TimerSystem

class AliensSystem:
    """Alien system"""
    def __init__(self, assets, alien_bullet_group, alien_group):
        self.assets = assets
        self.alien_bullets_group = alien_bullet_group
        self.alien_group = alien_group

        self.start_pos = (80, PLAY_AREA.bottom - 350)
        self.aliens_formation_list = []

        self.direction = pygame.Vector2(1, 0)
        self.aliens_move_timer = TimerSystem(ALIEN_TIMER)

        self.state = 'move_horizontal'
        self.current_alien = 0
        self.animation_index = 1

        self.shooting_enabled = False

    def update(self, dt):
        """Update alien formation"""
        self.aliens_move_timer.update(dt)
        self.update_aliens_formation()
        if len(self.alien_bullets_group) <= 0 and self.shooting_enabled:
            self.create_bullet()

    def update_aliens_formation(self):
        """Update formation"""
        if self.aliens_move_timer.active:
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
        self.aliens_move_timer.start()

    def create_bullet(self):
        """Alien shoot bullet"""
        alive_aliens = []
        for alien in self.aliens_formation_list:
            if alien.alive():
                alive_aliens.append(alien)

        alien = choice(alive_aliens)
        AlienBullet(alien.rect.midbottom, alien.bullets_images, self.alien_bullets_group)

    def move_horizontal(self, alien):
        """Move alien horizontal"""
        alien.pos.x += self.direction.x * HORIZONTAL_STEP

    def move_vertical(self, alien):
        """Move current alien vertical"""
        alien.pos.x += self.direction.x * (HORIZONTAL_STEP * 2)
        alien.pos.y += VERTICAL_STEP

    def check_wall_collision(self):
        """Check wall collision"""
        for alien in self.aliens_formation_list:
            if alien.alive():
                if alien.rect.right >= PLAY_AREA.right - FORMATION_MARGIN or alien.rect.left <= FORMATION_MARGIN:
                    return True
        return False

    def advance_cycle(self, wall_collision):
        """Advance cycle"""
        self.current_alien += 1

        if self.current_alien >= len(self.aliens_formation_list):
            self.current_alien = 0
            self.animation_index = 1 - self.animation_index

            if wall_collision:
                self.state = 'move_vertical'
                self.direction *= -1
            else:
                self.state = 'move_horizontal'

    def get_current_alien(self):
        """Get current alien"""
        return self.aliens_formation_list[self.current_alien]

    def find_next_alive_index(self):
        """Get next alive index of alien in formation"""
        start = self.current_alien
        index = start

        while True:
            index += 1

            if index >= len(self.aliens_formation_list):
                index = 0

            if self.aliens_formation_list[index].alive():
                return index

            if index == start:
                return None

    def update_alien_visuals(self, alien):
        """Update alien position and change alien image"""
        alien.rect.center = alien.pos
        alien.image = alien.images[self.animation_index]

    def create_alien_formation(self):
        """Create alien formation"""
        for alien_col, alien_type in enumerate(ALIENS_SETUP):
            for alien_row in range(NUM_ALIENS):
                self.aliens_formation_list.append(Alien(
                    (self.start_pos[0] + (alien_row * (ALIEN_STEP + ALIEN_SIZE[0])), 
                    self.start_pos[1] - (alien_col * (ALIEN_STEP + ALIEN_SIZE[1]))),
                    self.assets[alien_type]['images'],
                    self.assets[alien_type]['bullets'],
                    ALIEN_SCORE[alien_type],
                    self.alien_group
                ))