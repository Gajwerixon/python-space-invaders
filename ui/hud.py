import pygame

from config import *

class HUD:
    """Heads-Up Display"""
    def __init__(self, ship_img, font):
        self.font = font
        self.ship_img = ship_img

    def draw_hud(self, score_1, score_2, high_score, lives, credit, surface):
        """Draw HUD"""
        self.draw_top_hud(surface, score_1, score_2, high_score)
        self.draw_bottom_hud(surface, lives, credit)

    def draw_top_hud(self, surface, score_1, score_2, high_score):
        """Draw top hud"""
        self.draw_score_1(surface, score_1)
        self.draw_high_score(surface, high_score)
        self.draw_score_2(surface, score_2)

    def draw_score_1(self, surface, score_1):
        """Draw player_1 score"""
        # Text
        text_surface = self.font.render('S C O R E < 1 >', True, 'white')
        text_rect = text_surface.get_rect(topleft = (TOP_HUD_MARGIN_X, TOP_HUD_MARGIN_Y))
        surface.blit(text_surface, text_rect)

        # Score
        text_rect_pos_x = text_rect.centerx 
        text_rect_pos_y = text_rect.bottom  
        score_surface = self.font.render(f'{score_1:04d}', True, 'white')
        score_rect = score_surface.get_rect(midtop = (text_rect_pos_x, text_rect_pos_y + TEXT_SCORE_PADDING))
        surface.blit(score_surface, score_rect)

    def draw_high_score(self, surface, high_score):
        """Draw high score"""
        # Text
        text_surface = self.font.render('H I - S C O R E', True, 'white')
        text_rect = text_surface.get_rect(midtop = (WIDTH // 2, TOP_HUD_MARGIN_Y))
        surface.blit(text_surface, text_rect)

        # Score
        text_rect_pos_x = text_rect.centerx 
        text_rect_pos_y = text_rect.bottom  
        score_surface = self.font.render(f'{high_score:04d}', True, 'white')
        score_rect = score_surface.get_rect(midtop = (text_rect_pos_x, text_rect_pos_y + TEXT_SCORE_PADDING))
        surface.blit(score_surface, score_rect)

    def draw_score_2(self, surface, score_2):
        """Draw player_2 score"""
        # Text
        text_surface = self.font.render('S C O R E < 2 >', True, 'white')
        text_rect = text_surface.get_rect(topright = (WIDTH - TOP_HUD_MARGIN_X, TOP_HUD_MARGIN_Y))
        surface.blit(text_surface, text_rect)

        # Score
        text_rect_pos_x = text_rect.centerx 
        text_rect_pos_y = text_rect.bottom  
        score_surface = self.font.render(f'{score_2:04d}', True, 'white')
        score_rect = score_surface.get_rect(midtop = (text_rect_pos_x, text_rect_pos_y + TEXT_SCORE_PADDING))
        surface.blit(score_surface, score_rect)

    def draw_bottom_hud(self, surface, lives, credits):
        """Draw bottom hud"""
        self.draw_lives(surface, lives)
        self.draw_credit(surface, credits)

    def draw_lives(self, surface, lives):
        """Draw lives"""
        text_surface = self.font.render(f'{lives}', True, 'white')
        text_rect = text_surface.get_rect(topleft = (BOTTOM_HUD_MARGIN_X, HUD_BOTTOM_Y + BOTTOM_HUD_PADDING_Y))
        surface.blit(text_surface, text_rect)

        x, y = text_rect.topright
        x_start = x + 35
        
        if (lives - 1) != 0:
            for i in range(lives - 1):
                surface.blit(self.ship_img, (x_start + i * SHIP_IMG_OFFSET, y))

    def draw_credit(self, surface, credits):
        """Draw credit"""
        text_surface_1 = self.font.render(f'C R E D I T    {credits:02d}', True, 'white')
        text_rect_1 = text_surface_1.get_rect(topright = (WIDTH - BOTTOM_HUD_MARGIN_X, HUD_BOTTOM_Y + BOTTOM_HUD_PADDING_Y))
        surface.blit(text_surface_1, text_rect_1)

