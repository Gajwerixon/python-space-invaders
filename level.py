from entities.shield import Shield
from config import *

class Level:
    """Level class"""
    def __init__(self, shield_group):
        self.shield_group = shield_group

        self.create_shields()

    def create_shields(self):
        """Create shields"""
        margin = (WIDTH - (NUM_SHIELDS * SHIELD_SIZE[0]) - ((NUM_SHIELDS - 1) * SPACE_BETWEEN)) / 2

        for i in range(NUM_SHIELDS):
            Shield((margin + (i * (SPACE_BETWEEN + SHIELD_SIZE[0])), PLAY_AREA.bottom - SHIELD_BASE_OFFSET_Y), self.shield_group)