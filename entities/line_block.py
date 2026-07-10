import pygame

from config import LINES, EXPLOSIONS

class LineBlock(pygame.sprite.Sprite):
    """Line Block class"""
    def __init__(self, pos, block_id, group):
        super().__init__(group)
        self.image = pygame.Surface(LINES['size'])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft = pos)

        self.block_id = block_id
        self.group = group

    def apply_damage(self):
        """Handle line damage"""
        target_ids = self.get_target_ids()
        
        for block in self.group:
            if ( 
                block.block_id in target_ids 
                and EXPLOSIONS['line_damage_mask'][block.block_id] 
            ):
                block.kill()

    def get_target_ids(self):
        """Get target ids"""
        target_ids = set()

        for offset in EXPLOSIONS['line_damage_offsets']:
            target_id = self.block_id + offset

            if 0 <= target_id < LINES['count']:
                target_ids.add(target_id)

        return target_ids