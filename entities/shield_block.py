import pygame

from config import SHIELDS, EXPLOSIONS

class ShieldBlock(pygame.sprite.Sprite):
    """Shield Block class"""
    def __init__(self, pos, shield_id, grid_position, groups):
        super().__init__(groups)
        self.shield_blocks_group = groups
        self.image = pygame.Surface(((SHIELDS['block_size'])))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft = pos)

        self.shield_id = shield_id
        self.grid_position = grid_position

    def damage_shield(self, entity):
        """Handle shield damage"""
        target_grid_positions = self.get_target_positions(entity)
        self.destroy_target_blocks(target_grid_positions)

    def get_target_positions(self, entity):
        """Convert explosion shape to grid positions"""
        explosion_shape = EXPLOSIONS['shield_cache_shape'][entity]
        target_list = []

        for offset_x, offset_y in explosion_shape:
            target_list.append((
                self.grid_position[0] + offset_x, 
                self.grid_position[1] + offset_y
                )
            )

        return target_list
    
    def destroy_target_blocks(self, target_list):
        """Remove blocks hit by explosion"""
        target_set = set(target_list) 

        for block in self.shield_blocks_group:
            if block.shield_id != self.shield_id:
                continue

            if block.grid_position in target_set:
                block.kill()

    def damage_shield_alien(self):
        """Handle shield damage (by alien)"""
        for block in self.shield_blocks_group:
            if (block.shield_id == self.shield_id
                and block.grid_position[1] <= self.grid_position[1]):
                block.kill()