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