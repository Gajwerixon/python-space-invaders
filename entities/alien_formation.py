import pygame

from config import *

class AlienFormation:
    def __init__(self, assets, group):
        self.assets = assets
        self.alien_group = group

        self.alien_formation = []

        self.start_pos = (PLAY_AREA.left + 85, PLAY_AREA.top + 100)
        self.step = (50, 50)
        self.num_aliens = 10
        self.aliens = ('alien_3', 'alien_2', 'alien_2', 'alien_1', 'alien_1', )

        self.create_formation()

    def create_formation(self):
        for alien_row in range(len(self.aliens)):
            for alien_col in range(self.num_aliens):
                alien_instance = Alien(
                    (self.start_pos[0] + (alien_col * self.step[0]), 
                    self.start_pos[1] + (alien_row * self.step[1])),
                    self.assets[self.aliens[alien_row]]['images'],
                    self.assets[self.aliens[alien_row]]['bullets'],
                    self.alien_group
                )
                self.alien_formation.append(alien_instance)


class Alien(pygame.sprite.Sprite):
    """Alien class"""
    def __init__(self, pos, images, bullets, alien_group):
        super().__init__(alien_group)
        self.image = images[0]
        self.image = pygame.transform.scale(self.image, (36, 28))
        self.rect = self.image.get_rect(center = pos)

        self.bullets = bullets
