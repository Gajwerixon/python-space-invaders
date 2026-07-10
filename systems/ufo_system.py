from config import UFO, WIDTH
from entities.ufo import Ufo
from systems.timer_system import TimerSystem

class UfoSystem:
    """Ufo system class"""
    def __init__(self, ufo_image, ufo_group):
        self.image = ufo_image
        self.group = ufo_group

        self.phase = 'SPAWN_DELAY'
        self.ufo = None

        # Movement
        self.direction_x = 1
        self.speed = UFO['speed']
        self.spawn_pos = [(UFO['start_x'][0], UFO['start_y']), (UFO['start_x'][1], UFO['start_y'])]
        self.current_spawn_pos = 0

        # Timers
        self.spawn_ufo_timer = TimerSystem(UFO['spawn_timer'])
        self.spawn_ufo_timer.start()

        # Score
        self.score = UFO['score_values']

        # Events
        self.events = []

    def update(self, dt):
        """Update ufo base on current phase"""
        if self.phase == 'SPAWN_DELAY':
            self.spawn_ufo_timer.update(dt)
            if not self.spawn_ufo_timer.active:
                self.events.append('SPAWN_UFO')
                self.phase = 'SPAWNING'

        elif self.phase == 'SPAWNING':
            pass

        elif self.phase == 'ALIVE':
            self.ufo.update(dt)
            if self.outside_play_arena():
                self.handle_ufo_dead()

    def spawn_new_ufo(self, player_shots_count):
        """Spawn new Ufo"""
        shot_index = player_shots_count % len(self.score)
        assigned_points = self.score[shot_index]

        spawn_position = self.spawn_pos[self.current_spawn_pos]

        self.ufo = Ufo(
            self.image, 
            spawn_position, 
            self.direction_x,
            self.speed,
            assigned_points,
            self.group
        )

        self.phase = 'ALIVE'
        self.events.append('UFO_SPAWNED')
    
    def outside_play_arena(self):
        """Check if Ufo is outside play arena"""
        if self.direction_x == 1 and self.ufo.rect.left >= WIDTH:
            return True
        if self.direction_x == -1 and self.ufo.rect.right <= 0:
            return True
        return False
    
    def handle_ufo_dead(self):
        """Handle Ufo kill and change direction"""
        self.phase = 'SPAWN_DELAY'
        self.spawn_ufo_timer.start()
        self.events.append('UFO_DEAD')

        if self.ufo:
            self.ufo.kill()
            self.ufo = None

        self.direction_x *= -1
        
        self.current_spawn_pos = 1 - self.current_spawn_pos