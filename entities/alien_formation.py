import pygame

from config import *
from systems import Timer

class AlienFormation:
    """Alien formation"""
    def __init__(self, assets, group):
        self.assets = assets
        self.alien_group = group
        self.start_pos = (500, PLAY_AREA.top + 100)
        
        self.formation_list = []
        self.create_formation()

        self.velocity = FORMATION_VELOCITY
        self.direction = pygame.Vector2(1, 0)

        self.alien_timer = Timer(ALIEN_TIMER)

        self.current_row = -1
        self.current_alien = 0
        self.animation_index = 1

        self.cycle_completed = False

        self.state = 'move_horizontal'
        self.double_step_count = 0

    def update(self, dt):
        self.alien_timer.update(dt)
        self.update_formation(dt)
        self.update_alien_animation()

    def draw(self, surface):
        for alien in self.alien_group:
            surface.blit(alien.image, alien.rect.topleft)

    def update_formation(self, dt):
        """Update formation"""
        alien = self.get_current_alien()

        if self.state == 'move_horizontal' and not self.alien_timer.active:
            self.update_horizontal(alien, dt)

        if self.state == 'move_down' and not self.alien_timer.active:
            self.update_vertical(alien, dt)
        
    def get_current_alien(self):
        """Get current alien"""
        row = self.formation_list[self.current_row]

        if self.current_alien >= len(row):
            self.current_alien = 0
            self.current_row -= 1

            if self.current_row < -len(self.formation_list):
                self.current_row = -1
                self.cycle_completed = True
        
            row = self.formation_list[self.current_row]

        return row[self.current_alien]

    def update_horizontal(self, alien, dt):
        self.move_horizontal(alien, dt)
        if self.check_wall_collision():
            self.handle_collision()

    def move_horizontal(self, alien, dt):
        """Move alien horizontal"""     
        alien.pos.x += self.direction.x * self.velocity * dt
        alien.rect.center = alien.pos
        alien.image = alien.images[self.animation_index]

        self.current_alien += 1
        self.alien_timer.start()

    def check_wall_collision(self):
        """Check if any alien had collision with wall"""
        for alien_row in self.formation_list:
            for alien in alien_row:
                if alien.rect.right >= PLAY_AREA.right - 25 or alien.rect.left <= PLAY_AREA.left + 25:
                    return True

    def handle_collision(self):
        """Handle wall collision"""
        self.double_step_count = self.current_alien - 1 * abs(self.current_row)

        self.direction *= -1
        self.current_alien = 0
        self.current_row = -1

        self.state = 'move_down'
        self.alien_timer.active = False

    def update_vertical(self, alien, dt):
        """Update alien vertical"""
        step_multiplier = self.get_step_multiplier()
        if self.current_alien == 0 and self.current_row == -1 and step_multiplier == 1:
            self.state = 'move_horizontal'
        else:
            self.move_down(alien, step_multiplier, dt)

    def get_step_multiplier(self):
        """Return 2 if the alien move double timer in given direction else 1"""
        if self.double_step_count >= 0:
            self.double_step_count -= 1
            return 2
        return 1

    def move_down(self, alien, step_multiplier, dt):
        """Move alien down"""
        alien.pos.x += self.direction.x * step_multiplier * self.velocity * dt
        alien.pos.y += DESCENT_STEP_Y

        alien.rect.center = alien.pos
        alien.image = alien.images[self.animation_index]

        self.current_alien += 1
        self.alien_timer.start()

    def update_alien_animation(self):
        """Update alien animation"""
        # If the cycle is completed (all the aliens change the image)
        if self.cycle_completed:
            if self.animation_index == 1: self.animation_index = 0
            else: self.animation_index = 1
            self.cycle_completed = False

    def create_formation(self):
        """Create alien formation"""
        for alien_col in range(len(ALIENS_SETUP)):
            alien_row_list = []
            for alien_row in range(NUM_ALIENS):
                alien_row_list.append(Alien(
                    (self.start_pos[0] + (alien_row * (ALIEN_STEP + ALIEN_SIZE[0])), 
                    self.start_pos[1] + (alien_col * (ALIEN_STEP + ALIEN_SIZE[1]))),
                    self.assets[ALIENS_SETUP[alien_col]]['images'],
                    self.assets[ALIENS_SETUP[alien_col]]['bullets'],
                    self.alien_group
                ))
            self.formation_list.append(alien_row_list)

class Alien(pygame.sprite.Sprite):
    """Alien class"""
    def __init__(self, pos, images, bullets, alien_group):
        super().__init__(alien_group)
        self.images = images
        self.image = images[0]
        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.Vector2(self.rect.center)

        self.bullets = bullets
