import pygame

from config import *

class AdvanceTable:
    """Advance table class"""
    def __init__(self, font_assets, alien_assets, ufo_assets):
        self.font = font_assets
        self.alien = alien_assets
        self.ufo = ufo_assets

        self.start_game = False

        self.static_elements = [
            {
                'text': 'P L A Y',
                'pos': (WIDTH / 2, 220),
                'anchor': 'center'
            },
                        {
                'text': 'S P A C E       I N V A D E R S',
                'pos': (WIDTH / 2, 300),
                'anchor': 'center'
            },
                        {
                'text': '* S C O R E     A D V A N C E     T A B L E *',
                'pos': (WIDTH / 2, 380),
                'anchor': 'center'
            },
        ]

        self.img_elements = [
            {
            'img': self.ufo,
            'pos': (WIDTH / 2 - 100, 430),
            'score_pos': (WIDTH / 2 - 18, 430),
            'score': '= ? '
            },
            {
            'img': self.alien['alien_3']['images'][1],
            'pos': (WIDTH / 2 - 100, 480),
            'score_pos': (WIDTH / 2, 480),
            'score': '= 3 0'
            },
            {
            'img': self.alien['alien_2']['images'][0],
            'pos': (WIDTH / 2 - 100, 530),
            'score_pos': (WIDTH / 2, 530),
            'score': '= 2 0'
            },
            {
            'img': self.alien['alien_1']['images'][1],
            'pos': (WIDTH / 2 - 100, 580),
            'score_pos': (WIDTH / 2 - 7, 580),
            'score': '= 1 0'
            }
        ]

    def handle_events(self, event):
        ...

    def update(self, dt):
        ...

    def draw(self, surface):
        """Draw advance table"""
        for element in self.static_elements:
            self.draw_static_element(element['text'], element['pos'], surface)

        for element in self.img_elements:
            self.draw_image_element(element['img'], element['pos'], surface)
            self.draw_static_element(element['score'], element['score_pos'], surface, anchor='midright')

    def draw_static_element(self, text, pos, surface, anchor='center'):
        """Draw static element"""
        element_surface = self.font.render(text, True, 'white')
        element_rect = element_surface.get_rect(**{anchor: pos})
        surface.blit(element_surface, element_rect)

    def draw_image_element(self, img, pos, surface):
        """Draw image element"""
        image_rect = img.get_rect(center=pos)
        surface.blit(img, image_rect)
