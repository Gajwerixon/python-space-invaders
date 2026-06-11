from config import *

from entities.line_blocks import LineBlocks

class LineSystem:
    """LineBlocks class manager"""
    def __init__(self, group):
        self.line_group = group

    def create_line_blocks(self):
        """Create line blocks"""
        for line in range(NUM_LINES):
            pos_x = LINE_SIZE[0] * line
            pos_y = HUD_BOTTOM_Y - LINE_SIZE[1]
            LineBlocks((pos_x, pos_y), self.line_group)