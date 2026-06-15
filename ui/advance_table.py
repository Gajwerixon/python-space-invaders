import pygame

from config import *
from systems.timer_system import TimerSystem
from ui.animated_text import AnimatedText

class AdvanceTable:
    """Advance table class"""
    def __init__(self, font_assets, alien_assets, ufo_image):
        self.font = font_assets
        self.alien = alien_assets
        self.ufo = ufo_image

        self.phase = 'INTRO'
        self.continue_to_game = False

        self.letter_timer = TimerSystem(LETTER_TIMER)
        self.transition_timer = TimerSystem(ADVANCE_TABLE_TRANSITION_TIMER)

        self.intro_text = [ 
            AnimatedText('P L A Y', (WIDTH / 2 - 45, 200)),
            AnimatedText('S P A C E       I N V A D E R S', (WIDTH / 2 - 175, 280))
        ]

        self.score_text = [
            AnimatedText('= ?    M Y S T E R Y', (WIDTH / 2 - 70, 415)),
            AnimatedText('= 3 0     P O I N T S', (WIDTH / 2 - 70, 465)),
            AnimatedText('= 2 0     P O I N T S', (WIDTH / 2 - 70, 515)),
            AnimatedText('=  1 0     P O I N T S', (WIDTH / 2 - 70, 565))
        ]

        self.score_table_header = (
            '* S C O R E     A D V A N C E     T A B L E *',
            (WIDTH / 2, 380)
        )

        self.aliens_images = [
            (self.ufo, (WIDTH / 2 - 100, 430)),
            (self.alien['alien_3']['images'][1], (WIDTH / 2 - 100, 480)),
            (self.alien['alien_2']['images'][0], (WIDTH / 2 - 100, 530)),
            (self.alien['alien_1']['images'][1], (WIDTH / 2 - 100, 580)),
        ]
    
    def update(self, dt):
        """Update advance table"""
        self.letter_timer.update(dt)
        self.transition_timer.update(dt)

        if self.phase == 'INTRO':
            self.update_intro()

        elif self.phase == 'TRANSITION':
            self.update_transition()

        elif self.phase == 'SCORE_TABLE':
            self.update_score()
        
        elif self.phase == 'FINISHED':
            self.update_finished()

    def draw(self, surface):
        """Draw advance table"""
        self.draw_text_elements(self.intro_text, surface)

        if self.phase in ('SCORE_TABLE', 'FINISHED'):
            self.draw_score_table(surface)

    def update_intro(self):
        """Update INTRO phase"""
        self.update_animated_elements(self.intro_text)
        if all(element.done for element in self.intro_text):
            self.phase = 'TRANSITION'
            self.transition_timer.start()

    def update_transition(self):
        """Update TRANSITION phase"""
        if not self.transition_timer.active:
            self.phase = 'SCORE_TABLE'

    def update_score(self):
        """Update SCORE phase"""
        self.update_animated_elements(self.score_text)
        if all(element.done for element in self.score_text):
            self.phase = 'FINISHED'
            self.transition_timer.start()

    def update_finished(self):
        """Update FINISHED phase"""
        if not self.transition_timer.active:
            self.continue_to_game = True

    def update_animated_elements(self, elements):
        """Update animated elements"""
        if not self.letter_timer.active:
            for element in elements:
                if not element.done:
                    element.update()
                    self.letter_timer.start()
                    break

    def draw_score_table(self, surface):
        """Draw SCORE_TABLE"""
        text, pos = self.score_table_header
        self.blit_text(text, pos, surface)
        
        for img, pos in self.aliens_images:
            self.blit_img(img, pos, surface)

        self.draw_text_elements(self.score_text, surface)

    def draw_text_elements(self, elements, surface):
        """Draw text elements"""
        for element in elements:
            self.blit_text(
                element.display_text,
                element.pos,
                surface,
                element.anchor
            )

    def blit_text(self, text, pos, surface, anchor='center'):
        """Blit text on the surface"""
        element_surface = self.font.render(text, True, 'white')
        element_rect = element_surface.get_rect(**{anchor: pos})
        surface.blit(element_surface, element_rect)

    def blit_img(self, img, pos, surface):
        """Blit image on the surface"""
        image_rect = img.get_rect(center=pos)
        surface.blit(img, image_rect)