import pygame

from config import *
from systems.timer_system import TimerSystem
from ui.animated_text import AnimatedText

class Menu:
    """Menu class"""
    def __init__(self, font):
        self.font = font

        self.animation_done = False
        self.selection_confirmed = False
        self.player_options = [1, 2]
        self.selected_option = 0

        self.letter_timer = TimerSystem(LETTER_TIMER)
        self.static_elements = [('S E L E C T  N U M B E R  O F  P L A Y E R S', (WIDTH / 2, HEIGHT / 2 - 25))]
        self.animated_elements = [
            AnimatedText('<  1   O R   2   P L A Y E R S  >', 
                         (WIDTH / 2 - 170, HEIGHT / 2 + 60)),
            AnimatedText('1   P L A Y E R       1    C O I N',
                         (WIDTH / 2 - 141, HEIGHT / 2 + 120)),
            AnimatedText('2  P L A Y E R S   2   C O I N S',
                         (WIDTH / 2 - 144, HEIGHT / 2 + 180))
        ]

    def handle_events(self, event):
        """Handle menu events"""
        if self.animation_done:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and self.selected_option != 1:
                    self.selected_option = 1
                elif event.key == pygame.K_UP and self.selected_option != 0:
                    self.selected_option = 0
                elif event.key == pygame.K_RETURN:
                    self.selection_confirmed = True

    def update(self, dt):
        """Update menu"""
        self.letter_timer.update(dt)

        if not self.letter_timer.active:
            for element in self.animated_elements:
                if not element.done:
                    element.update()
                    self.letter_timer.start()
                    break
        
        if all(element.done for element in self.animated_elements):
            self.animation_done = True

    def draw(self, surface):
        """Draw menu"""
        for text, pos in self.static_elements:
            self.draw_element(text, pos, surface)
        
        for element in self.animated_elements:
            self.draw_element(
                element.display_text,
                element.pos,
                surface,
                element.anchor
            )

        if self.animation_done:
            self.draw_number_of_players_marker(surface)

    def draw_element(self, text, pos, surface, anchor='center'):
        """Draw static element"""
        element_surface = self.font.render(text, True, 'white')
        element_rect = element_surface.get_rect(**{anchor: pos})
        surface.blit(element_surface, element_rect)

    def draw_number_of_players_marker(self, surface):
        """Draw current player marker"""
        menu_index = self.player_options[self.selected_option]
        self.draw_element('*', 
                          (self.animated_elements[menu_index].pos[0] - 30,
                            self.animated_elements[menu_index].pos[1]),
                            surface, 
                            anchor='topleft'
        )

    @property
    def get_num_players(self):
        """Return num of player"""
        return self.player_options[self.selected_option]