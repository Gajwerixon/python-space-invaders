import pygame

class SoundSystem:
    def __init__(self, sounds):
        self.sounds = sounds

    # --- Player ---
    def player_shoot_play(self):
        self.sounds['player']['shoot'].play()

    def player_dead_play(self):
        self.sounds['player']['dead'].play()

    # --- Aliens ---
    def alien_dead_play(self):
        pass

    def aliens_movement_play(self):
        pass

    # --- UFO ---
    def ufo_movement_play(self):
        pass

    def ufo_dead_play(self):
        pass

    # --- UI ---
    def ui_next_phase_play(self):
        """Play the next_phase sound in UI objects"""
        self.sounds['ui']['next_phase'].play()

    def ui_switch_option_play(self):
        """Play the switch_option sound in UI objects"""
        self.sounds['ui']['switch_option'].play()