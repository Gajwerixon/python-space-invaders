import pygame

class SoundSystem:
    def __init__(self, sounds):
        self.sounds = sounds

    def player_shoot_play(self):
        self.sounds['player']['shoot'].play()

    def alien_dead_play(self):
        self.sounds['alien']['dead'].play()

    def player_dead_play(self):
        self.sounds['player']['dead'].play()