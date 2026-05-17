from entities.shield import Shield
from config import *

class Level:
    """Level class"""
    def __init__(self, shield_group):
        self.shield_group = shield_group

        self.create_shields()

    def create_shields(self):
        """Create shields"""
        for i in range(NUM_SHIELDS):
            Shield((SHIELD_MARGIN_X + i * SPACE_BETWEEN, SHIELD_MARGIN_Y), self.shield_group)

    