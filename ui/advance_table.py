import pygame

from config import *
from systems.timer_system import TimerSystem

class AdvanceTable:
    """Advance table class"""
    def __init__(self, font_assets, alien_assets, ufo_assets):
        self.font = font_assets
        self.alien = alien_assets
        self.ufo = ufo_assets

        self.start_game = False
        self.animation_done = True
        self.animation_2_done = False

        self.animated_elements = [
            {
                'text': 'P L A Y',
                'current_text': '',
                'index': 0,
                'pos': (WIDTH / 2 - 45, 200),
                'anchor': 'topleft',
                'done': True,
            },
            {
                'text': 'S P A C E       I N V A D E R S',
                'current_text': '',
                'index': 0,
                'pos': (WIDTH / 2 - 175, 280),
                'anchor': 'topleft',
                'done': True,
            }
        ]

        self.static_elements = [
            {
                'text': '* S C O R E     A D V A N C E     T A B L E *',
                'pos': (WIDTH / 2, 380),
                'anchor': 'center',
                'type': 'text'
            },
            {
                'img': self.ufo,
                'pos': (WIDTH / 2 - 100, 430),
                'type': 'img'
            },
            {
                'img': self.alien['alien_3']['images'][1],
                'pos': (WIDTH / 2 - 100, 480),
                'type': 'img'
            },
            {
                'img': self.alien['alien_2']['images'][0],
                'pos': (WIDTH / 2 - 100, 530),
                'type': 'img'
            },
            {
                'img': self.alien['alien_1']['images'][1],
                'pos': (WIDTH / 2 - 100, 580),
                'type': 'img'
            }
        ]

        self.score_elements = [
            {
                'text': '= ?    M Y S T E R Y',
                'current_text': '',
                'pos': (WIDTH / 2 - 70, 415),
                'index': 0,
                'anchor': 'topleft',
                'done': False
            },
            {
                'text': '= 3 0     P O I N T S',
                'current_text': '',
                'pos': (WIDTH / 2 - 70, 465),
                'index': 0,
                'anchor': 'topleft',
                'done': False
            },
            {
                'text': '= 2 0     P O I N T S',
                'current_text': '',
                'pos': (WIDTH / 2 - 70, 515),
                'index': 0,
                'anchor': 'topleft',
                'done': False
            },
            {
                'text': '=  1 0     P O I N T S',
                'current_text': '',
                'pos': (WIDTH / 2 - 70, 565),
                'index': 0,
                'anchor': 'topleft',
                'done': False
            }
        ]

        self.letter_timer = TimerSystem(LETTER_TIMER)
        self.static_elements_timer = TimerSystem(0.75)
        self.start_game_timer = TimerSystem(0.75)
        self.static_elements_timer.active = True
    
    def handle_events(self, event):
        """Handle advance table events"""
        ...

    def update(self, dt):
        """Update advance table"""
        self.letter_timer.update(dt)
        self.static_elements_timer.update(dt)
        self.start_game_timer.update(dt)
        if self.animation_2_done and not self.start_game_timer.active:
            self.start_game = True

    def draw(self, surface):
        """Draw advance table"""
        for element in self.animated_elements:
            if element['done']:
                self.draw_static_element(element['text'], element['pos'], surface, anchor=element['anchor'])
                continue

            if element['index'] >= len(element['text']):
                element['done'] = True

                if all(element['done'] for element in self.animated_elements):
                    if not self.animation_done:
                        self.static_elements_timer.start()
                        self.animation_done = True
            
            self.draw_animated_element(element, surface)
        
        if self.animation_done and not self.static_elements_timer.active:
            for element in self.static_elements:
                if element['type'] == 'img':
                    self.draw_image_element(element['img'], element['pos'], surface)
                else:
                    self.draw_static_element(element['text'], element['pos'], surface, anchor=element['anchor'])
            
            for element in self.score_elements:
                if element['done']:
                    self.draw_static_element(element['text'], element['pos'], surface, anchor=element['anchor'])
                    continue

                if element['index'] >= len(element['text']):
                    element['done'] = True
                    if not self.animation_2_done:
                        if all(item['done'] for item in self.score_elements):
                            self.animation_2_done = True
                            self.start_game_timer.start()
            
                self.draw_animated_element(element, surface)

    def draw_static_element(self, text, pos, surface, anchor='center'):
        """Draw static element"""
        element_surface = self.font.render(text, True, 'white')
        element_rect = element_surface.get_rect(**{anchor: pos})
        surface.blit(element_surface, element_rect)

    def draw_image_element(self, img, pos, surface):
        """Draw image element"""
        image_rect = img.get_rect(center=pos)
        surface.blit(img, image_rect)

    def draw_animated_element(self, item, surface):
        """Draw text letter by letter"""
        if not self.letter_timer.active:
            item['current_text'] += item['text'][item['index']]
            item['index'] += 1

            self.letter_timer.start()

        self.draw_static_element(item['current_text'], item['pos'], surface, anchor='topleft')