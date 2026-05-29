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
        self.velocity = FORMATION_VELOCITY
        self.direction = pygame.Vector2(1, 0)
        self.alien_timer = Timer(ALIEN_TIMER)

        # Current variables
        self.current_alien = 0
        self.animation_index = 1
        self.cycle_completed = False

    def update(self, dt):
        """Update alien formation"""
        self.alien_timer.update(dt)
        self.update_formation(dt)
        if self.cycle_completed:
            self.toggle_animation_frame()
            self.cycle_completed = False

    def draw(self, surface):
        """Draw alien formation"""
        for alien in self.alien_group:
            surface.blit(alien.image, alien.rect.topleft)

    def update_formation(self, dt):
        """Update formation"""
        if self.state == 'move_horizontal' and not self.alien_timer.active:
            self.move_horizontal(dt)
            if self.check_wall_collision():
                self.handle_collision()
            else:
                self.advance_cycle()

        if self.state == 'move_down' and not self.alien_timer.active:
            self.move_down(dt)
            self.advance_cycle()
            if self.cycle_completed:
                self.state = 'move_horizontal'

    def move_horizontal(self, dt):
        """Move alien horizontal"""
        alien = self.formation_list[self.current_alien]

        alien.pos.x += self.direction.x * self.velocity * dt
        alien.rect.center = alien.pos
        alien.image = alien.images[self.animation_index]

    def check_wall_collision(self):
        """Check if any alien had collision with wall"""
        for alien in self.formation_list:
            if alien.rect.right >= PLAY_AREA.right - 25 or alien.rect.left <= PLAY_AREA.left + 25:
                return True

    def handle_collision(self):
        """Handle wall collision"""
        for i, alien in enumerate(self.formation_list):
            if i > self.current_alien:
                break

            alien.double_step = True

        self.direction *= -1
        self.current_alien = 0

        self.state = 'move_down'
        self.alien_timer.active = False

    def advance_cycle(self):
        """Change to next alien"""
        self.current_alien += 1

        if self.current_alien >= len(self.formation_list):
            self.current_alien = 0
            self.cycle_completed = True

        self.alien_timer.start()

    def move_down(self, dt):
        """Move alien down"""
        alien = self.formation_list[self.current_alien]

        if alien.double_step:
            step = 2
            alien.double_step = False
        else:
            step = 1

        alien.pos.x += self.direction.x * step * self.velocity * dt
        alien.pos.y += DESCENT_STEP_Y

        alien.rect.center = alien.pos
        alien.image = alien.images[self.animation_index]
    
    def toggle_animation_frame(self):
        """Change alien animation index"""
        if self.animation_index == 1: self.animation_index = 0
        else: self.animation_index = 1

    def create_formation(self):
        """Create alien formation"""
        for alien_col in range(len(ALIENS_SETUP)):
            for alien_row in range(NUM_ALIENS):
                self.formation_list.append(Alien(
                    (self.start_pos[0] + (alien_row * (ALIEN_STEP + ALIEN_SIZE[0])), 
                    self.start_pos[1] - (alien_col * (ALIEN_STEP + ALIEN_SIZE[1]))),
                    self.assets[ALIENS_SETUP[alien_col]]['images'],
                    self.assets[ALIENS_SETUP[alien_col]]['bullets'],
                    self.alien_group
                ))

class Alien(pygame.sprite.Sprite):
    """Alien class"""
    def __init__(self, pos, images, bullets, alien_group):
        super().__init__(alien_group)
        self.images = images
        self.image = images[0]
        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.Vector2(self.rect.center)

        self.bullets = bullets
        
        # Flags
        self.double_step = False