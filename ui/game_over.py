from systems.timer_system import TimerSystem
from ui.animated_text import AnimatedText

from config import PLAY_AREA, LETTER_TIMER

class GameOver:
    """GameOver class"""
    def __init__(self, font):
        self.font = font
        self.new_game_timer = TimerSystem(5)
        self.text = AnimatedText(
            'G A M E  O V E R',
            (235, PLAY_AREA.top),
        )
        self.start_new_game = False
        self.letter_timer = TimerSystem(LETTER_TIMER)
        self.start_timer = True

    def update(self, dt):
        """Update GameOver """
        self.new_game_timer.update(dt)
        self.letter_timer.update(dt)

        if not self.letter_timer.active:
            if not self.text.done:
                self.text.update()
                self.letter_timer.start()

        if self.text.done and self.start_timer:
            self.new_game_timer.start()
            self.start_timer = False
        
        if self.text.done and not self.start_timer:
            if not self.new_game_timer.active:
                self.start_new_game = True
                return

    def draw(self, surface):
        """Draw GameOver elements on the screen"""
        element_surface = self.font.render(self.text.display_text, True, 'white')
        element_rect = element_surface.get_rect(**{self.text.anchor: self.text.pos})
        surface.blit(element_surface, element_rect)