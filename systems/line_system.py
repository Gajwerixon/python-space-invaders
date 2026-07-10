from config import LINES, PLAY_AREA

from entities.line_block import LineBlock

class LineSystem:
    """LineBlocks system class"""
    def __init__(self, group):
        self.line_group = group

    def create_line_blocks(self):
        """Create line blocks"""
        for block in range(LINES['count']):
            pos_x = LINES['size'][0] * block
            pos_y = PLAY_AREA.bottom + LINES['size'][1]
            LineBlock((pos_x, pos_y), block, self.line_group)