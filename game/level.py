from entities.shield import Shield
from config import *

class Level:
    """Level class"""
    def __init__(self, shield_group):
        self.shield_blocks_group = shield_group
        self.shield = Shield(self.shield_blocks_group)
        self.shield.create_shield_blocks()