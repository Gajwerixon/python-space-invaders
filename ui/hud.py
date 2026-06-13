from config import TOP_HUD, BOTTOM_HUD, WIDTH, PLAY_AREA

class HUD:
    """Heads-Up Display"""
    def __init__(self, ship_img, font):
        self.font = font
        self.ship_img = ship_img

    def draw_hud(self, score_1, score_2, high_score, lives, credit, surface):
        """Draw HUD"""
        self.draw_top_hud(score_1, score_2, high_score, surface)
        self.draw_bottom_hud(lives, credit, surface)

    def draw_top_hud(self, score_1, score_2, high_score, surface):
        """Draw top hud"""
        self.draw_score(score_1, 'S C O R E < 1 >', 
                        (TOP_HUD['margin_x'], TOP_HUD['margin_y']), 
                        'topleft', surface)
        self.draw_score(high_score, 'H I - S C O R E', 
                        (WIDTH // 2, TOP_HUD['margin_y']), 
                        'midtop', surface)
        self.draw_score(score_2, 'S C O R E < 2 >', 
                        (WIDTH - TOP_HUD['margin_x'], TOP_HUD['margin_y']), 
                        'topright', surface)

    def draw_bottom_hud(self, lives, credits, surface):
        """Draw bottom hud"""
        self.draw_lives(surface, lives)
        self.draw_credit(surface, credits)

    def draw_score(self, label, text, pos, anchor, surface):
        """Draw score"""
        text_rect = self.blit_text(surface, text, pos, anchor)
        
        self.blit_text(surface, f'{label:04d}', 
                       (text_rect.centerx, text_rect.bottom + TOP_HUD['score_padding']),
                       anchor='midtop')

    def draw_lives(self, surface, lives):
        """Draw lives"""
        text_rect = self.blit_text(surface, str(lives), 
                       (BOTTOM_HUD['margin_x'], PLAY_AREA.bottom + BOTTOM_HUD['padding_y']),
                       'topleft')
        
        x, y = text_rect.topright
        x_start = x + 35
        
        if (lives - 1) != 0:
            for i in range(lives - 1):
                surface.blit(self.ship_img, (x_start + i * BOTTOM_HUD['ship_offset'], y))

    def draw_credit(self, surface, credits):
        """Draw credit"""
        pos = (WIDTH - BOTTOM_HUD['margin_x'], PLAY_AREA.bottom + BOTTOM_HUD['padding_y'])
        self.blit_text(surface, f'C R E D I T    {credits:02d}', pos, 'topright')

    def blit_text(self, surface, text, pos, anchor='center'):
        """Blit text and return rect postion"""
        surf = self.render_text(text)
        rect = surf.get_rect(**{anchor: pos})
        surface.blit(surf, rect)
        return rect

    def render_text(self, text):
        """Render text"""
        return self.font.render(text, True, 'white')