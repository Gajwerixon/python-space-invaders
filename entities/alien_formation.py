import pygame

from config import *
from systems import Timer

class AlienFormation:
    """Alien formation"""
    def __init__(self, assets, group):
        self.assets = assets
        self.alien_group = group
        self.start_pos = (64, PLAY_AREA.top + 100)
        
        self.formation_list = []
        self.create_formation()

        self.velocity = 256
        self.direction = pygame.Vector2(1, 0)

        self.alien_timer = Timer(0.025)

        self.current_row = -1
        self.current_alien = 0
        self.animation_index = 0
        self.cycle_completed = False
        self.wall_touched = False

    def update(self, dt):
        self.alien_timer.update(dt)
        self.formation_logic(dt)

    def draw(self, surface):
        for alien in self.alien_group:
            surface.blit(alien.image, alien.rect.topleft)

    def formation_logic(self, dt):
        """Formation logic"""
        if not self.alien_timer.active and not self.wall_touched:
            row = self.formation_list[self.current_row]
            if self.current_alien >= len(row):
                self.current_alien = 0
                self.current_row -= 1
                if self.current_row < -len(self.formation_list):
                    self.current_row = -1
                    self.cycle_completed = True
            
                row = self.formation_list[self.current_row]
            
            alien = row[self.current_alien]

            alien.pos.x += self.direction.x * self.velocity * dt
            alien.rect.center = alien.pos
            alien.image = alien.images[self.animation_index]

            self.current_alien += 1
            self.alien_timer.start()
        
        if self.cycle_completed:
            self.animation_index += 1
            if self.animation_index > 1:
                self.animation_index = 0
            self.cycle_completed = False
        
        if not self.wall_touched:
            for alien_row in self.formation_list:
                for alien in alien_row:
                    if alien.rect.right >= PLAY_AREA.right - 25 or alien.rect.left <= PLAY_AREA.left + 25:
                        self.wall_touched = True
                        self.direction *= -1

                        self.current_alien = 0
                        self.current_row = -1
                        break
        
        if self.wall_touched:
            if not self.alien_timer.active:
                row = self.formation_list[self.current_row]
                if self.current_alien >= len(row):
                    self.current_alien = 0
                    self.current_row -= 1
                    if self.current_row < -len(self.formation_list):
                        self.current_row = -1
                        self.cycle_completed = True
                        self.wall_touched = False
                        return
                
                    row = self.formation_list[self.current_row]

                alien = row[self.current_alien]
                
                alien.pos.x += self.direction.x * self.velocity * dt
                alien.pos.y += 25
                alien.rect.center = alien.pos
                alien.image = alien.images[self.animation_index]

                self.current_alien += 1
                self.alien_timer.start()
        
    
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
