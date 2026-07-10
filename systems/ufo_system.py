from config import UFO, WIDTH
from entities.ufo import Ufo
from systems.timer_system import TimerSystem

class UfoSystem:
    def __init__(self, ufo_image, ufo_group):
        self.image = ufo_image
        self.group = ufo_group

        self.phase = 'SPAWN_DELAY'
        self.ufo = None

        self.direction_x = 1
        self.speed = UFO['speed']

        self.spaw_pos = [(UFO['start_x'][0], UFO['start_y']), (UFO['start_x'][1], UFO['start_y'])]
        self.current_spawn_pos = 0

        self.score = UFO['score_values']
        self.current_score_index = 0

        self.events = []

        self.spawn_ufo_timer = TimerSystem(UFO['spawn_timer'])
        self.spawn_ufo_timer.start()

    def update(self, dt):
        """Update"""
        if self.phase == 'SPAWN_DELAY':
            self.spawn_ufo_timer.update(dt)
            if not self.spawn_ufo_timer.active:
                self.spawn_new_ufo()
                self.phase = 'ALIVE'
                self.events.append('UFO_SPAWNED')

        elif self.phase == 'ALIVE':
            self.ufo.update(dt)
            if self.outside_play_arena():
                self.handle_ufo_dead()
                self.events.append('UFO_DEAD')

    def spawn_new_ufo(self):
        """Spawn new Ufo"""
        self.ufo = Ufo(
            self.image, 
            self.spaw_pos[self.current_spawn_pos], 
            self.direction_x,
            self.speed,
            self.score[self.current_score_index],
            self.group
        )
    
    def outside_play_arena(self):
        """Check if Ufo is outside play arena"""
        if self.direction_x == 1 and self.ufo.rect.left >= WIDTH:
            return True
        if self.direction_x == -1 and self.ufo.rect.right <= 0:
            return True
        return False
    
    def handle_ufo_dead(self):
        """Handle Ufo kill"""
        self.phase = 'SPAWN_DELAY'
        self.spawn_ufo_timer.start()
        self.events.append('UFO_DEAD')

        if self.ufo:
            self.ufo.kill()
            self.ufo = None

        self.direction_x *= -1

        self.current_score_index = (self.current_score_index + 1) % len(self.score)
        
        self.current_spawn_pos = 1 - self.current_spawn_pos