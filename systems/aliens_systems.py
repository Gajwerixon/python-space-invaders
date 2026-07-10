import pygame
from config import ALIENS_FORMATION, ALIENS_MOVEMENT, PLAY_AREA
from random import choice
from entities.alien import Alien
from entities.alien_bullet import AlienBullet
from systems.timer_system import TimerSystem

class AliensSystem:
    """AlienSystem class"""
    def __init__(self, assets, alien_bullet_group, alien_group, current_level):
        self.assets = assets
        self.alien_bullets_group = alien_bullet_group
        self.alien_group = alien_group
        self.current_level = current_level

        # Formation
        self.start_pos = (80, PLAY_AREA.bottom - 350)
        self.aliens_formation_list = []
        self.num_aliens = 0

        # Movement
        self.direction = pygame.Vector2(1, 0)
        self.state = 'move_horizontal'
        self.current_alien = 0
        self.animation_index = 0
        self.wall_collision_triggered = False

        # Timers
        self.base_speed = self.get_base_speed()
        self.aliens_move_timer = TimerSystem(self.base_speed)
        self.shoot_timer = TimerSystem(1)

        # Shooting
        self.shooting_enabled = False
        self.max_number_of_bullets = 1

        # Events
        self.events = []

    def update(self, dt):
        """Update formation"""
        self.aliens_move_timer.update(dt)
        self.shoot_timer.update(dt)

        if not self.alien_group:
            self.events.append('ALL_ALIENS_DEAD')
            return
        
        self.update_movement()
        self.formation_shoot()

    def update_movement(self):
        """Update formation movement"""
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

        if (alien.rect.right >= PLAY_AREA.right - ALIENS_FORMATION['margin'] or 
            alien.rect.left <= ALIENS_FORMATION['margin']):
            self.wall_collision_triggered = True

        self.advance_cycle()
        self.aliens_move_timer.start()

    def formation_shoot(self):
        """Formatin shoot base of number of aliens"""
        alive_ratio = len(self.alien_group) / self.num_aliens

        if alive_ratio >= 0.4:
            self.max_number_of_bullets = 1
            self.shoot_timer.set_duration(1.2)
        elif alive_ratio >= 0.2:
            self.max_number_of_bullets = 2
            self.shoot_timer.set_duration(0.8)
        else:
            self.max_number_of_bullets = 3
            self.shoot_timer.set_duration(0.4)

        if (
            self.shooting_enabled
            and len(self.alien_bullets_group) < self.max_number_of_bullets
            and not self.shoot_timer.active
        ):
            self.create_bullet()
            self.shoot_timer.start()

    def advance_cycle(self):
        """Advance index to the next living alien, skipping dead ones"""
        self.current_alien += 1
        total_aliens = len(self.aliens_formation_list)

        if self.current_alien >= total_aliens:
            self._end_of_turn_reset()

        while not self.aliens_formation_list[self.current_alien].alive():
            self.current_alien += 1
            if self.current_alien >= total_aliens:
                self._end_of_turn_reset()

    def _end_of_turn_reset(self):
        """Reset index and update formation state"""
        self.current_alien = 0
        self.animation_index = 1 - self.animation_index

        self.events.append("PLAY_NEXT_SOUND")

        if self.wall_collision_triggered:
            self.state = "move_vertical"
            self.direction.x *= -1
            self.wall_collision_triggered = False
        else:
            self.state = "move_horizontal"

    def create_bullet(self):
        """Select a random alien from the frontline columns to fire"""
        lowest_aliens = self._get_lowest_aliens()

        if lowest_aliens:
            alien = choice(lowest_aliens)
            AlienBullet(
                (alien.rect.centerx, alien.rect.bottom + 25), 
                alien.bullets_images, 
                self.alien_bullets_group
            )

    def _get_lowest_aliens(self):
        """Filter the formation to retrieve only the lowest alien from each column"""
        columns = {}

        for alien in self.alien_group:
            col = alien.grid_pos[1]
            if col not in columns or alien.pos.y > columns[col].pos.y:
                columns[col] = alien
        return list(columns.values())

    def update_speed(self):
        """Calculate movement speed adjustments"""
        if self.num_aliens == 0:
            return
        
        alive_ratio = len(self.alien_group) / self.num_aliens
        new_delay = self.base_speed * (0.9 + 0.7 * alive_ratio)
        self.aliens_move_timer.set_duration(new_delay)

    def get_base_speed(self):
        """Get starting difficulty delay based on current wave level"""
        base_delay = ALIENS_MOVEMENT["timer"]

        level_multiplier = 1 - (self.current_level - 1) * 0.05
        level_multiplier = max(level_multiplier, 0.6)

        delay = base_delay * level_multiplier

        return delay

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