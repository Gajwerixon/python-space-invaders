from config import TOP_HUD, BOTTOM_HUD, WIDTH, PLAY_AREA

class HUD:
    """Heads-Up Display"""
    def __init__(self, ship_img, font, digits):
        self.font = font
        self.digits = digits
        self.ship_img = ship_img

    def draw_hud(self, score_1, score_2, high_score, lives, credit, surface, show_lives):
        self.draw_top_hud(score_1, score_2, high_score, surface)
        self.draw_bottom_hud(lives, credit, surface, show_lives)

    def draw_top_hud(self, score_1, score_2, high_score, surface):
        self.draw_score(
            'S C O R E < 1 >', 
            score_1,
            (TOP_HUD['margin_x'], TOP_HUD['margin_y']), 
            'topleft', 
            surface
        )

        self.draw_score(
            'H I - S C O R E', 
            high_score, 
            (WIDTH // 2, TOP_HUD['margin_y']), 
            'midtop', 
            surface
        )

        self.draw_score(
            'S C O R E < 2 >', 
            score_2,
            (WIDTH - TOP_HUD['margin_x'], TOP_HUD['margin_y']), 
            'topright', 
            surface
        )

    def draw_bottom_hud(self, lives, credits, surface, show_lives):
        if show_lives:
            self.draw_lives(surface, lives)

        self.draw_credit(surface, credits)

    def draw_score(self, text, value, pos, anchor, surface):
        text_rect = self.blit_text(surface, text, pos, anchor)
    
        digits = self.format_number(value)
        start_pos = (text_rect.left + 50, text_rect.bottom + 16)

        self.draw_number(digits, start_pos, 'top_hud', surface)

    def draw_lives(self, surface, lives):
        text_rect = self.blit_text(
            surface, 
            str(lives), 
            (BOTTOM_HUD['left_margin'], PLAY_AREA.bottom + BOTTOM_HUD['padding_y']),
            'topleft'
        )
        
        x, y = text_rect.topright
        x_start = x + 28
        
        if (lives - 1) != 0:
            for i in range(lives - 1):
                surface.blit(self.ship_img, (x_start + i * BOTTOM_HUD['ship_offset'], y))

    def draw_credit(self, surface, credits):
        pos = (WIDTH - BOTTOM_HUD['right_margin'], PLAY_AREA.bottom + BOTTOM_HUD['padding_y'])
        rect = self.blit_text(surface, f'C R E D I T', pos, 'topright')

        digits = self.format_number(credits, length=2)
        start_pos = (rect.right + 20, rect.top + 2) 
        self.draw_number(digits, start_pos, 'bottom_hud', surface)

    def blit_text(self, surface, text, pos, anchor='center'):
        """Blit text and return rect postion"""
        surf = self.font.render(text, True, 'white')
        rect = surf.get_rect(**{anchor: pos})
        surface.blit(surf, rect)
        return rect
    
    def format_number(self, value, length=4):
        return str(value).zfill(length)
    
    def draw_number(self, digits, start_pos, hud, surface):
        x, y = start_pos

        for digit in digits:
            img = self.digits[hud][int(digit)]
            surface.blit(img, (x, y))
            x += img.get_width() + 3