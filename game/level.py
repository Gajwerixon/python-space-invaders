from entities.player import Player
from systems.shield_system import ShieldSystem
from systems.line_system import LineSystem
from systems.aliens_systems import AliensSystem
from systems.effect_system import EffectSystem
from systems.collision_system import CollisionSystem
from systems.timer_system import TimerSystem
from systems.ufo_system import UfoSystem

class Level:
    """Level class"""
    def __init__(self, groups, assets, sound_system):
        self.groups = groups
        self.assets = assets
        self.sound_system = sound_system

        self.phase = 'START'
        self.spawn_player_timer = TimerSystem(1.75)
        self.next_level_timer = TimerSystem(1.5)

        self.lives = 3
        self.score_1 = 0
        self.score_2 = 0
        self.current_level = 1
        self.player_shots_count = 0

        self.player = None
        self.shield_system = None
        self.line_system = None
        self.aliens_system = None
        self.ufo_system = None

        self.effect_system = EffectSystem(self.assets.effects, self.groups['effects'])
        self.collision_system = CollisionSystem(self.groups, self.effect_system)

        self.manually_updated_groups = {'aliens', 'ufo'}

    def update(self, dt):
        """Update level"""
        self.spawn_player_timer.update(dt)

        states = {
            'START': self.update_start,
            'GAMEPLAY': self.update_gameplay,
            'RESET': self.update_reset,
            'NEXT_LEVEL': self.update_next_level,
            'GAME_OVER': lambda _: None
        }
        
        states[self.phase](dt)

    def draw(self, surface):
        """Draw elements"""
        for group in self.groups.values():
            group.draw(surface)

    def update_start(self, dt):
        """Update start"""
        self.aliens_system.update(dt)

        if self.try_spawn_player():
            self.aliens_system.shooting_enabled = True
            self.phase = 'GAMEPLAY'

    def update_gameplay(self, dt):
        """Update gameplay"""
        self.aliens_system.update(dt)
        self.ufo_system.update(dt)
        self.collision_system.update()
        self.update_groups(dt)
        self.handle_events()

    def update_reset(self, dt):
        """Update reset"""
        self.update_groups(dt)
        self.ufo_system.update(dt)

        if self.try_spawn_player():
            self.phase = 'GAMEPLAY'

    def update_next_level(self, dt):
        """Update next level"""
        self.next_level_timer.update(dt)
        if self.next_level_timer.active:
            if self.player:
                self.player.update(dt)
            return
        
        self.current_level += 1
        self.create_level()
        self.phase = 'START'    

    def update_groups(self, dt):
        """Update groups except aliens_group"""
        for name, group in self.groups.items():
            if name not in self.manually_updated_groups:
                group.update(dt)

    def handle_events(self):
        """Handle events"""
        self.handle_collision_events()
        self.handle_aliens_events()
        self.handle_player_events()
        self.handle_ufo_events()

    def handle_collision_events(self):
        for event in self.collision_system.events:
            event_type = event[0]
            if event_type == "PLAYER_DEAD":
                self.handle_player_dead()
                self.sound_system.player_dead_play()

            elif event_type == 'UFO_DEAD':
                self.ufo_system.handle_ufo_dead()
                self.score_1 += event[1]

            elif event_type == 'ALIEN_DEAD':
                self.score_1 += event[1]
                self.aliens_system.update_speed()
                self.sound_system.alien_dead_play()
        
        self.collision_system.events.clear()

    def handle_aliens_events(self):
        """Handle aliens events"""
        for event in self.aliens_system.events:
            if event == 'ALL_ALIENS_DEAD':
                self.phase = 'NEXT_LEVEL'
                self.next_level_timer.start()
            elif event == 'PLAY_NEXT_SOUND':
                pass
        
        self.aliens_system.events.clear()

    def handle_player_events(self):
        if not self.player:
            return

        for event in self.player.events:
            if event == 'PLAYER_SHOOT':
                self.sound_system.player_shoot_play()
                self.player_shots_count += 1
            
        self.player.events.clear()

    def handle_ufo_events(self):
        """Handle UfoSystem events"""
        for event in self.ufo_system.events:
            if event == 'SPAWN_UFO':
                self.ufo_system.spawn_new_ufo(self.player_shots_count)
            elif event == 'UFO_SPAWNED':
                self.sound_system.ufo_movement_start()
            elif event == 'UFO_DEAD':
                self.sound_system.ufo_movement_stop()

        self.ufo_system.events.clear()

    def try_spawn_player(self):
        """Try spawn new player"""
        if not self.spawn_player_timer.active:
            self.spawn_player()
            return True
        return False

    def handle_player_dead(self):
        """Handle player dead"""
        if self.player:
            for bullet in self.player.bullets:
                bullet.kill()
            self.player.kill()
            self.player = None

        self.lives -= 1
        if self.lives > 0: 
            self.phase = "RESET"
            self.spawn_player_timer.start()
        else:
            self.phase = 'GAME_OVER'
            self.sound_system.ufo_movement_stop()

    def spawn_player(self):
        """Spawn new player"""
        self.player = Player(
            self.assets.player['player_img'], 
            self.groups['player_bullets'], 
            self.groups['player']
        )
        
    def create_level(self):
        """Create level"""
        for group in self.groups.values():
            group.empty()

        self.shield_system = ShieldSystem(self.groups['shields'])
        self.line_system = LineSystem(self.groups['lines'])
        self.aliens_system = AliensSystem(
            self.assets.aliens, 
            self.groups['alien_bullets'], 
            self.groups['aliens'],
            self.current_level
        )
        self.ufo_system = UfoSystem(self.assets.ufo['image'], self.groups['ufo'])

        self.shield_system.create_shield_blocks()
        self.line_system.create_line_blocks()
        self.aliens_system.create_alien_formation()

        self.spawn_player_timer.start()