import pygame

from config import *

class Shield:
    """Shields class manager"""
    def __init__(self, group):
        self.shield_block_group = group

    def create_shield_blocks(self):
        """Create shields blocks"""
        start_pos = (100, PLAY_AREA.bottom - 200)

        for shield in range(NUM_SHIELDS):
            for current_col, shield_row in enumerate(SHIELD_SHAPE):
                for current_row, shield_block in enumerate(shield_row):
                    if shield_block == 1:
                        pos_x = start_pos[0] + SHIELD_BLOCK_SIZE[0] * current_row + shield * SPACE_BETWEEN
                        pos_y = start_pos[1] + SHIELD_BLOCK_SIZE[1] * current_col
                        ShieldBlocks((pos_x, pos_y), self.shield_block_group)

class ShieldBlocks(pygame.sprite.Sprite):
    """Shield Blocks class"""
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface(((SHIELD_BLOCK_SIZE)))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft = pos)