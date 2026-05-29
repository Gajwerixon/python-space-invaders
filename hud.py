import pygame

from config import *

class HUD:
    """Heads-Up Display"""
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font('assets/font.ttf', FONT_SIZE)

        # Line
        self.line_image = pygame.Surface((WIDTH, LINE_WIDTH))
        self.line_image.fill((255, 255, 255))
        self.line_rect= self.line_image.get_rect(topleft = (0, HUD_BOTTOM_Y))

        # Lives (ship images)
        self.ship_image = pygame.image.load('assets/entities/player/player.png').convert_alpha()
        self.ship_image = pygame.transform.scale(self.ship_image, SHIP_IMG_SIZE)

    def draw_hud(self, surface):
        """Draw HUD"""
        self.draw_top_hud(surface)
        self.draw_bottom_hud(surface)

    def draw_top_hud(self, surface):
        """Draw top hud"""
        self.draw_score_1(surface)
        self.draw_high_score(surface)
        self.draw_score_2(surface)

    def draw_score_1(self, surface):
        """Draw player_1 score"""
        # Text
        text_surface = self.font.render('S C O R E < 1 >', True, 'white')
        text_rect = text_surface.get_rect(topleft = (TOP_HUD_MARGIN_X, TOP_HUD_MARGIN_Y))
        surface.blit(text_surface, text_rect)

        # Score
        text_rect_pos_x = text_rect.centerx 
        text_rect_pos_y = text_rect.bottom  
        score_surface = self.font.render(f'{self.game.score:04d}', True, 'white')
        score_rect = score_surface.get_rect(midtop = (text_rect_pos_x, text_rect_pos_y + TEXT_SCORE_PADDING))
        surface.blit(score_surface, score_rect)

    def draw_high_score(self, surface):
        """Draw high score"""
        # Text
        text_surface = self.font.render('H I - S C O R E', True, 'white')
        text_rect = text_surface.get_rect(midtop = (WIDTH // 2, TOP_HUD_MARGIN_Y))
        surface.blit(text_surface, text_rect)

        # Score
        text_rect_pos_x = text_rect.centerx 
        text_rect_pos_y = text_rect.bottom  
        score_surface = self.font.render(f'{self.game.score:04d}', True, 'white')
        score_rect = score_surface.get_rect(midtop = (text_rect_pos_x, text_rect_pos_y + TEXT_SCORE_PADDING))
        surface.blit(score_surface, score_rect)

    def draw_score_2(self, surface):
        """Draw player_2 score"""
        # Text
        text_surface = self.font.render('S C O R E < 2 >', True, 'white')
        text_rect = text_surface.get_rect(topright = (WIDTH - TOP_HUD_MARGIN_X, TOP_HUD_MARGIN_Y))
        surface.blit(text_surface, text_rect)

    def draw_bottom_hud(self, surface):
        """Draw bottom hud"""
        surface.blit(self.line_image, self.line_rect)

        self.draw_lives(surface)
        self.draw_credit(surface)

    def draw_lives(self, surface):
        """Draw lives"""
        lives = self.game.lives

        text_surface = self.font.render(f'{lives}', True, 'white')
        text_rect = text_surface.get_rect(topleft = (BOTTOM_HUD_MARGIN_X, HUD_BOTTOM_Y + BOTTOM_HUD_PADDING_Y))
        surface.blit(text_surface, text_rect)

        x, y = text_rect.topright
        x_start = x + 35
        
        if (lives - 1) != 0:
            for i in range(lives - 1):
                surface.blit(self.ship_image, (x_start + i * SHIP_IMG_OFFSET, y))

    def draw_credit(self, surface):
        """Draw credit"""
        text_surface_1 = self.font.render(f'C R E D I T    {self.game.credit:02d}', True, 'white')
        text_rect_1 = text_surface_1.get_rect(topright = (WIDTH - BOTTOM_HUD_MARGIN_X, HUD_BOTTOM_Y + BOTTOM_HUD_PADDING_Y))
        surface.blit(text_surface_1, text_rect_1)

