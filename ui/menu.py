import pygame

from config import *
from systems.timer_system import TimerSystem

class Menu:
    """Menu class"""
    def __init__(self, font):
        self.font = font

        self.start_game = False
        self.player_options = [
            {"players": 1,
             "menu_index": 1},
            {"players": 2,
             "menu_index": 2}
        ]
        self.selected_option = 0

        self.letter_timer = TimerSystem(LETTER_TIMER)
        self.animation_done = False
        self.static_info = [('S E L E C T  N U M B E R  O F  P L A Y E R S', (WIDTH / 2, HEIGHT / 2 - 25))]
        self.animated_info = [
            {'text': '<  1   O R   2   P L A Y E R S  >', 
             'pos': (WIDTH / 2 - 170, HEIGHT / 2 + 60),
             'current_text': '', 'index': 0, 'done': False},

            {'text': '1   P L A Y E R       1    C O I N', 
             'pos': (WIDTH / 2 - 141, HEIGHT / 2 + 120),
             'current_text': '', 'index': 0, 'done': False},

            {'text': '2  P L A Y E R S   2   C O I N S', 
             'pos': (WIDTH / 2 - 144, HEIGHT / 2 + 180),
             'current_text': '', 'index': 0, 'done': False},
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
                    self.start_game = True

    def update(self, dt):
        """Update menu"""
        self.letter_timer.update(dt)

    def draw(self, surface):
        """Draw menu"""
        for text, pos in self.static_info:
            self.draw_element(text, pos, surface)
        
        for item in self.animated_info:
            if item['done']:
                self.draw_element(item['text'], item['pos'], surface, anchor='topleft')
                if self.animation_done:
                    self.draw_number_of_players_marker(surface)
                continue

            if item['index'] >= len(item['text']):
                item['done'] = True
                if all(item['done'] for item in self.animated_info):
                    self.animation_done = True

            self.draw_animated_element(item, surface)

    def draw_element(self, text, pos, surface, anchor='center'):
        """Draw static element"""
        element_surface = self.font.render(text, True, 'white')
        element_rect = element_surface.get_rect(**{anchor: pos})
        surface.blit(element_surface, element_rect)

    def draw_animated_element(self, item, surface):
        """Draw text letter by letter"""
        if not self.letter_timer.active:
            item['current_text'] += item['text'][item['index']]
            item['index'] += 1

            self.letter_timer.start()

        self.draw_element(item['current_text'], item['pos'], surface, anchor='topleft')

    def draw_number_of_players_marker(self, surface):
        """Draw current player marker"""
        menu_index = self.player_options[self.selected_option]['menu_index']
        self.draw_element('*', 
                          (self.animated_info[menu_index]['pos'][0] - 30,
                            self.animated_info[menu_index]['pos'][1]),
                            surface, 
                            anchor='topleft'
        )

    @property
    def get_num_players(self):
        """Return num of player"""
        return self.player_options[self.selected_option]['players']