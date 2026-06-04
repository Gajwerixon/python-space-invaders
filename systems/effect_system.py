from entities.effect import Effect
from entities.animated_effect import AnimatedEffect

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

    def spawn_alien_bullet_shield_explosion(self, pos, duration):
        """Spaw explosion effect between alien bullet and shield"""
        Effect(self.assets['alien_bullet_fx'], pos, duration, self.group, anchor='center')

    def spawn_player_explosion(self, pos, full_duration, frame_duration):
        """Spawn player explosion animated effect"""
        AnimatedEffect(self.assets['player_explosion'], pos, full_duration, frame_duration, self.group)