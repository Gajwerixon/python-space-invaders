import pygame
from config import *
from systems.timer_system import TimerSystem

class AlienBullet(pygame.sprite.Sprite):
    """Alien Bullet class"""
    def __init__(self, pos, images, groups):
        super().__init__(groups)
        self.images = images
        self.image = images[0]
        self.rect = self.image.get_rect(midbottom = pos)
        self.pos = pygame.Vector2(self.rect.center)

        self.speed = ALIEN_BULLET_SPEED

        self.animation_frame = 0
        self.image_timer = TimerSystem(0.078125)
        self.image_timer.start()

    def update(self, dt):
        """Update bullet"""
        self.image_timer.update(dt)
        self.movement(dt)
        self.change_image_frame()

    def change_image_frame(self):
        """Change image frame"""
        if not self.image_timer.active:
            self.animation_frame += 1
            if self.animation_frame >= len(self.images):
                self.animation_frame = 0
            self.image = self.images[self.animation_frame]
            self.image_timer.start()

    def movement(self, dt):
        """Bullet movement"""
        self.pos.y += self.speed * dt
        self.rect.center = self.pos