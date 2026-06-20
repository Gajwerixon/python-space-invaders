from config import LINES, PLAY_AREA

from entities.line_blocks import LineBlocks

class LineSystem:
    """LineBlocks class manager"""
    def __init__(self, group):
        self.line_group = group

    def create_line_blocks(self):
        """Create line blocks"""
        for block in range(LINES['count']):
            pos_x = LINES['size'][0] * block
            pos_y = PLAY_AREA.bottom + LINES['size'][1]
            LineBlocks((pos_x, pos_y), block, self.line_group)