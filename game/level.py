from entities.player import Player
from systems.shield_system import ShieldSystem
from systems.line_system import LineSystem
from systems.aliens_systems import AliensSystem
from systems.effect_system import EffectSystem
from systems.collision_system import CollisionSystem
from systems.timer_system import TimerSystem

from config import *

class Level:
    """Level class"""
    def __init__(self, groups, assets):
        self.groups = groups
        self.assets = assets

        self.phase = 'START'
        self.player_timer = TimerSystem(1.5)

        self.player = None
        self.shield_system = ShieldSystem(self.groups['shields'])
        self.line_system = LineSystem(self.groups['lines'])
        self.effect_system = EffectSystem(
            self.assets.effects, 
            self.groups['effects']
        )
        self.collision_system = CollisionSystem(self.groups, self.effect_system)
        self.aliens_system = AliensSystem(
            self.assets.aliens, 
            self.groups['alien_bullets'], 
            self.groups['aliens']
        )

        self.initialize_level()

        """
        'START' -> load (shields, lines, aliens) [allow alines to move not shoot] {f_start} ->
        wait 1 secound... ->
        load spawn player + [allow aliens to shoot] {f_}
        ->
        """

    def handle_events(self, event):
        """Handle level events"""
        pass

    def update(self, dt):
        """Update level"""
        self.player_timer.update(dt)

        if self.phase == 'START':
            self.aliens_system.update(dt)

            if not self.player_timer.active:
                self.start_playing()
                self.phase = 'PLAYING'

        elif self.phase == 'PLAYING':
            self.aliens_system.update(dt)
            self.collision_system.update()

            for name, group in self.groups.items():
                if name == 'aliens':
                    continue
                group.update(dt)

            for event in self.collision_system.events:
                if event == "PLAYER_DEAD":
                    self.phase = "RESET"
                    self.player_timer.start()

        elif self.phase == 'RESET':
            for name, group in self.groups.items():
                if name == 'aliens':
                    continue
                group.update(dt)

            self.collision_system.events = []
            if not self.player_timer.active:
                self.player = Player(
                    self.assets.player['player_img'], 
                    self.groups['player_bullets'], 
                    self.groups['player']
                )
                self.phase = 'PLAYING'

    def draw(self, surface):
        """Draw level"""
        for group in self.groups.values():
            group.draw(surface)

    def initialize_level(self):
        """Initialize new level"""
        self.shield_system.create_shield_blocks()
        self.line_system.create_line_blocks()
        self.aliens_system.create_alien_formation()

        self.player_timer.start()

    def start_playing(self):
        """START -> PLAYING"""
        self.player = Player(
                    self.assets.player['player_img'], 
                    self.groups['player_bullets'], 
                    self.groups['player']
                )

        self.aliens_system.shooting_enabled = True