import pygame
from config import ALIENS_FORMATION, ALIENS_MOVEMENT, PLAY_AREA
from random import choice
from entities.alien import Alien
from entities.alien_bullet import AlienBullet
from systems.timer_system import TimerSystem

class AliensSystem:
    """System zarządzający formacją kosmitów (w stylu Space Invaders)"""
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
        self.animation_index = 0
        self.shooting_enabled = False

        self.num_aliens = 0
        self.events = []
        self.wall_collision_triggered = False

    def update(self, dt):
        """Update formation"""
        self.aliens_move_timer.update(dt)

        if not self.alien_group:
            self.events.append('ALL_ALIENS_DEAD')
            return
        
        self.update_aliens_formation()

        if len(self.alien_bullets_group) <= 0 and self.shooting_enabled:
            self.create_bullet()

    def update_aliens_formation(self):
        """Update alien formation"""
        if self.aliens_move_timer.active:
            return
        
        alien = self.aliens_formation_list[self.current_alien]
        
        if self.state == 'move_horizontal':
            alien.pos.x += self.direction.x * ALIENS_MOVEMENT['horizontal_step']
        else:
            alien.pos.x += self.direction.x * ALIENS_MOVEMENT["horizontal_step"] * 2
            alien.pos.y += ALIENS_MOVEMENT['vertical_step']

        alien.rect.center = alien.pos
        alien.image = alien.images[self.animation_index]

        # self.events.append('PLAY_NEXT_SOUND')

        if (alien.rect.right >= PLAY_AREA.right - ALIENS_FORMATION['margin'] or 
            alien.rect.left <= ALIENS_FORMATION['margin']):
            self.wall_collision_triggered = True

        self.advance_cycle()
        self.aliens_move_timer.start()

    def advance_cycle(self):
        """Advance cycle"""
        self.current_alien += 1
        total_aliens = len(self.aliens_formation_list)

        if self.current_alien >= total_aliens:
            self._end_of_turn_reset()

        while not self.aliens_formation_list[self.current_alien].alive():
            self.current_alien += 1
            if self.current_alien >= total_aliens:
                self._end_of_turn_reset()

    def _end_of_turn_reset(self):
        """Reset index and update formation state at"""
        self.current_alien = 0
        self.animation_index = 1 - self.animation_index

        if self.wall_collision_triggered:
            self.state = "move_vertical"
            self.direction.x *= -1
            self.wall_collision_triggered = False
        else:
            self.state = "move_horizontal"

    def create_bullet(self):
        """Create bullet"""
        lowest_aliens = self.get_lowest_aliens()
        if lowest_aliens:
            alien = choice(lowest_aliens)
            AlienBullet(
                (alien.rect.centerx, alien.rect.bottom + 25), 
                alien.bullets_images, 
                self.alien_bullets_group
            )

    def get_lowest_aliens(self):
        """Zwraca listę najniższych żywych obcych z każdej kolumny"""
        columns = {}
        for alien in self.alien_group:
            col = alien.grid_pos[1]
            if col not in columns or alien.pos.y > columns[col].pos.y:
                columns[col] = alien
        return list(columns.values())

    def update_speed(self):
        """Update speed"""
        if self.num_aliens == 0:
            return
        
        alive_ratio = len(self.alien_group) / self.num_aliens
        new_delay = ALIENS_MOVEMENT['timer'] * (0.3 + 0.7 * alive_ratio)
        self.aliens_move_timer.set_duration(new_delay)

    def create_alien_formation(self):
        """Create formation"""
        for alien_col, alien_type in enumerate(ALIENS_FORMATION['layout']):
            for alien_row in range(ALIENS_FORMATION['num_aliens']):
                pos_x = self.start_pos[0] + (alien_row * (ALIENS_FORMATION['spacing'] + ALIENS_FORMATION['size'][0]))
                pos_y = self.start_pos[1] - (alien_col * (ALIENS_FORMATION['spacing'] + ALIENS_FORMATION['size'][1]))
                
                alien = Alien(
                    (pos_x, pos_y),
                    self.assets[alien_type]['images'],
                    self.assets[alien_type]['bullets'],
                    ALIENS_FORMATION['scores'][alien_type],
                    self.alien_group,
                    (alien_col, alien_row)
                )
                self.aliens_formation_list.append(alien)

        self.num_aliens = len(self.alien_group)