import pygame

from config import *
from entities.ufo import Ufo
from systems.timer_system import TimerSystem

class UfoSystem:
    def __init__(self, ufo_image, ufo_group):
        self.image = ufo_image
        self.group = ufo_group

        self.phase = 'SPAWN_DELAY'
        self.ufo = None
        self.spaw_pos = [(25, PLAY_AREA.top + 25), (WIDTH - 25, PLAY_AREA.top + 25)]
        self.current_spawn_pos = 0

        self.direction_x = 1
        self.speed = 100

        self.score = [100, 50, 50, 100, 150, 100, 100, 50, 300, 100, 100, 100, 50, 150, 100, 50]
        self.current_score_index = 0

        self.spawn_ufo_timer = TimerSystem(5)
        self.spawn_ufo_timer.start()

    def update(self, dt):
        """Update"""
        if self.phase == 'SPAWN_DELAY':
            self.spawn_ufo_timer.update(dt)
            if not self.spawn_ufo_timer.active:
                self.spawn_new_ufo()
                self.phase = 'ALIVE'

        elif self.phase == 'ALIVE':
            self.ufo.movement(dt)
            if self.outside_play_arena():
                self.handle_ufo_kill()
                self.phase = 'SPAWN_DELAY'
                self.spawn_ufo_timer.start()

    def spawn_new_ufo(self):
        """Spawn new Ufo"""
        self.ufo = Ufo(self.image, 
                       self.spaw_pos[self.current_spawn_pos], 
                       self.direction_x,
                       self.speed,
                       self.score[self.current_score_index],
                       self.group)
        
        self.spawn_ufo_timer.active = True
    
    def outside_play_arena(self):
        """Check if Ufo is outside play arena"""
        if self.ufo.rect.left <= 0 or self.ufo.rect.right >= WIDTH:
            return True
        return False
    
    def handle_ufo_kill(self):
        """Handle Ufo kill"""
        self.ufo.kill()
        self.ufo = None

        self.direction_x *= -1

        self.current_score_index += 1
        if self.current_score_index > len(self.score):
            self.current_score_index = 0
        
        self.current_spawn_pos = 1 if self.current_spawn_pos == 0 else 0