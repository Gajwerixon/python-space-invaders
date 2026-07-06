import pygame

from config import ALIENS_FORMATION, ALIENS_MOVEMENT, PLAY_AREA
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
        self.aliens_move_timer = TimerSystem(ALIENS_MOVEMENT['timer'])

        self.state = 'move_horizontal'
        self.current_alien = 0
        self.animation_index = 1

        self.shooting_enabled = False
        self.num_aliens = 0

        self.events = []

    def update(self, dt):
        """Update alien formation"""
        if not self.alien_group:
            self.events.append('ALL_ALIENS_DEAD')
            return
        
        self.aliens_move_timer.update(dt)
        self.update_aliens_formation()
        if len(self.alien_bullets_group) <= 0 and self.shooting_enabled:
            self.create_bullet()

    def update_aliens_formation(self):
        """Update formation"""
        if self.aliens_move_timer.active:
            return
        
        alien = self.get_current_alien()
        
        if self.state == 'move_horizontal':
            self.move_horizontal(alien)
        else:
            self.move_vertical(alien)

        self.update_alien_visuals(alien)

        wall_collision = self.check_wall_collision()
        self.advance_cycle(wall_collision)
        self.aliens_move_timer.start()

    def update_speed(self):
        alive_ratio = len(self.alien_group) / 54
        new_delay = ALIENS_MOVEMENT['timer'] * (0.5 + 0.5 * alive_ratio)

        self.aliens_move_timer.set_duration(new_delay)

    def get_lowest_aliens(self):
        """Return the lowest alive alien from each column."""
        columns = {}

        for alien in self.get_alive_aliens():
            columns.setdefault(alien.grid_pos[1], alien)

        return list(columns.values())

    def create_bullet(self):
        """Alien shoot bullet"""
        alien = choice(self.get_lowest_aliens())
        AlienBullet(
            (alien.rect.centerx, alien.rect.bottom + 25), 
            alien.bullets_images, 
            self.alien_bullets_group
        )

    def move_horizontal(self, alien):
        """Move alien horizontal"""
        alien.pos.x += self.direction.x * ALIENS_MOVEMENT['horizontal_step']

    def move_vertical(self, alien):
        """Move current alien vertical"""
        alien.pos.x += self.direction.x * (ALIENS_MOVEMENT['horizontal_step'] * 2)
        alien.pos.y += ALIENS_MOVEMENT['vertical_step']

    def check_wall_collision(self):
        """Check wall collision"""
        for alien in self.get_alive_aliens():
            if alien.rect.right >= PLAY_AREA.right - ALIENS_FORMATION['margin'] or alien.rect.left <= ALIENS_FORMATION['margin']:
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

    def update_alien_visuals(self, alien):
        """Update alien position and change alien image"""
        alien.rect.center = alien.pos
        alien.image = alien.images[self.animation_index]

    def get_alive_aliens(self):
        return [alien for alien in self.aliens_formation_list if alien.alive()]

    def create_alien_formation(self):
        """Create alien formation"""
        for alien_col, alien_type in enumerate(ALIENS_FORMATION['layout']):
            for alien_row in range(ALIENS_FORMATION['num_aliens']):
                self.aliens_formation_list.append(Alien(
                    (self.start_pos[0] + (alien_row * (ALIENS_FORMATION['spacing'] + ALIENS_FORMATION['size'][0])), 
                    self.start_pos[1] - (alien_col * (ALIENS_FORMATION['spacing'] + ALIENS_FORMATION['size'][1]))),
                    self.assets[alien_type]['images'],
                    self.assets[alien_type]['bullets'],
                    ALIENS_FORMATION['scores'][alien_type],
                    self.alien_group,
                    (alien_col, alien_row)
                ))