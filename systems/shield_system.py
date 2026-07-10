from config import SHIELDS, PLAY_AREA
from entities.shield_block import ShieldBlock

class ShieldSystem:
    """ShieldBlocks system class"""
    def __init__(self, group):
        self.shield_block_group = group

    def create_shield_blocks(self):
        """Create shields blocks"""
        start_pos = (80, PLAY_AREA.bottom - 150)

        for shield in range(SHIELDS['count']):
            for current_col, shield_row in enumerate(SHIELDS['shape']):
                for current_row, shield_block in enumerate(shield_row):
                    if shield_block == 1:
                        pos_x = start_pos[0] + SHIELDS['block_size'][0] * current_row + shield * SHIELDS['spacing']
                        pos_y = start_pos[1] + SHIELDS['block_size'][1] * current_col
                        ShieldBlock((pos_x, pos_y), shield, (current_row, current_col), self.shield_block_group)