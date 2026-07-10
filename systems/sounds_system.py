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
        self.sounds['alien']['dead'].play()

    def aliens_movement_play(self, index):
        self.sounds['alien']['movement'][index].play()

    # --- UFO ---
    def ufo_movement_start(self):
        self.sounds['ufo']['movement'].play(loops=-1)

    def ufo_movement_stop(self):
        self.sounds['ufo']['movement'].stop()

    # --- UI ---
    def ui_next_phase_play(self):
        """Play the next_phase sound in UI objects"""
        self.sounds['ui']['next_phase'].play()

    def ui_switch_option_play(self):
        """Play the switch_option sound in UI objects"""
        self.sounds['ui']['switch_option'].play()