class AnimatedText:
    """AnimatedText class"""
    def __init__(self, text, pos, anchor='topleft'):
        self.text = text
        self.pos = pos
        self.anchor = anchor
        self.current_text = ''
        self.index = 0
        self.done = False

    def update(self):
        """Update animated text"""
        if self.done:
            return
        
        self.current_text += self.text[self.index]
        self.index += 1

        if self.index >= len(self.text):
            self.done = True

    @property
    def display_text(self):
        """Display current text"""
        return self.text if self.done else self.current_text