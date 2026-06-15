import pygame
from systems.timer_system import TimerSystem

class AnimatedEffect(pygame.sprite.Sprite):
    """Effect class"""
    def __init__(self, images, pos, full_duration, frame_duration, type, groups):
        super().__init__(groups)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=pos)

        self.animation_timer = TimerSystem(full_duration)
        self.frame_animation_timer = TimerSystem(frame_duration)
        self.animation_index = 0

        self.animation_timer.start()
        self.frame_animation_timer.start()

        self.type = type

    def update(self, dt):
        """Update explosion"""
        self.animation_timer.update(dt)
        self.frame_animation_timer.update(dt)
        self.animation()

    def animation(self):
        """Animation"""
        if self.animation_timer.active:
            if not self.frame_animation_timer.active:
                self.animation_index = 1 - self.animation_index
                self.image = self.images[self.animation_index]
                self.frame_animation_timer.start()
        else:
            self.kill()