import pygame

from config import *

class HUD:
    """Heads-Up Display"""
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font('assets/font.ttf', 25)

        # Line
        self.line_image = pygame.Surface((WIDTH, LINE_WIDTH))
        self.line_image.fill(GREEN)
        self.line_rect= self.line_image.get_rect(topleft = LINE_POS)

        # Lives (ship images)
        self.ship_image = pygame.image.load('assets/entities/player/player.png').convert_alpha()
        self.ship_image = pygame.transform.scale(self.ship_image, SHIP_IMG_SIZE)
        green = pygame.Surface(self.ship_image.get_size()).convert_alpha()
        green.fill(GREEN)
        self.ship_image.blit(green, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    def draw_hud(self, surface):
        """Draw HUD"""
        self.draw_top_hud(surface)
        self.draw_bottom_hud(surface)

    def draw_top_hud(self, surface):
        """Draw top hud"""
        ...

    def draw_bottom_hud(self, surface):
        """Draw bottom hud"""
        surface.blit(self.line_image, self.line_rect)

        self.draw_lives(surface)
        self.draw_credit(surface)

    def draw_lives(self, surface):
        """Draw lives"""
        lives = self.game.lives

        text_surface = self.font.render(f'{lives}', True, 'white')
        text_rect = text_surface.get_rect(topleft = LIVES_TEXT_POS)
        surface.blit(text_surface, text_rect)

        for i in range(lives):
            surface.blit(self.ship_image, (SHIP_IMG_POS[0] + i * SHIP_IMG_OFFSET, SHIP_IMG_POS[1]))

    def draw_credit(self, surface):
        """Draw credit"""
        text_surface_1 = self.font.render(f'C R E D I T    {self.game.credit:02d}', True, 'white')
        text_rect_1 = text_surface_1.get_rect(topright = CREDIT_TEXT_POS)
        surface.blit(text_surface_1, text_rect_1)

