from entities.effect import Effect

class EffectSystem:
    """Effect Manager"""
    def __init__(self, effect_assets, group):
        self.assets = effect_assets
        self.group = group

    def player_bullets_aliens_fx(self, pos, duration):
        """Spawn explosion between player bullet and alien"""
        Effect(self.assets['alien_explosion_fx'], pos, duration, self.group)
    
    def spaw_bullet_shield_explosion(self, pos, duration):
        """Spawn explosion effect between bullet and shield"""
        Effect(self.assets['player_bullet_fx'], pos, duration, self.group)

    def spawn_player_bullet_miss_explosion(self, pos, duration):
        """Spaw explosion effect after bullet miss"""
        Effect(self.assets['player_bullet_fx'], pos, duration, self.group, anchor='midtop')

    def spawn_alien_bullet_miss_explosion(self, pos, duration):
        """Spawn explosion effect after alien bullet miss"""
        Effect(self.assets['alien_bullet_fx'], pos, duration, self.group, anchor='midbottom')