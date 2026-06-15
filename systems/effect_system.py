from entities.effect import Effect
from entities.animated_effect import AnimatedEffect

class EffectSystem:
    """Effect Manager"""
    def __init__(self, effect_assets, group):
        self.assets = effect_assets
        self.group = group

    def player_bullets_aliens_fx(self, pos, duration):
        """Spawn explosion between player_bullets and aliens"""
        Effect(
            self.assets['alien_explosion_fx'], 
            pos, 
            duration,
            'player_bullets_aliens_fx', 
            self.group
        )
    
    def player_bullets_shield_blocks_fx(self, pos, duration):
        """Spawn explosion between player bullets and shield blocks"""
        Effect(
            self.assets['player_bullet_fx'], 
            pos, 
            duration,
            'player_bullets_shield_blocks', 
            self.group
        )

    def player_bullets_miss_fx(self, pos, duration):
        """Spawn explosion after player bullets hit PLAY_AREA top"""
        Effect(
            self.assets['player_bullet_fx'], 
            pos, 
            duration,
            'player_bullets miss', 
            self.group, 
            anchor='midtop'
        )

    def alien_bullets_miss_fx(self, pos, duration):
        """Spawn explosion effect after alien bullets hit PLAY_AREA bottom"""
        Effect(
            self.assets['alien_bullet_fx'], 
            pos, 
            duration,
            'alien_bullets miss',
            self.group, 
            anchor='midbottom'
        )

    def alien_bullet_shield_fx(self, pos, duration):
        """Spaw explosion between alien bullets and shield blocks"""
        Effect(
            self.assets['alien_bullet_fx'], 
            pos, 
            duration,
            'alien_bullets shield_blocks', 
            self.group, 
            anchor='center'
        )

    def player_hit_fx(self, pos, full_duration, frame_duration):
        """Spawn explosion AnimtedEffect after player was hit"""
        AnimatedEffect(
            self.assets['player_explosion'], 
            pos, 
            full_duration, 
            frame_duration, 
            'player_explosion', 
            self.group
        )

    def player_bullets_alien_bullets_fx(self, pos, duration):
        """Spawn explosion after player bullets hit alien bullets"""
        Effect(
            self.assets['player_bullet_fx'], 
            pos, 
            duration,
            'player_bullets alien_bullets', 
            self.group
        )

    def player_bullets_ufo_fx(self, pos, duration):
        """Spawn explosion after player_bullets hit ufo"""
        Effect(
            self.assets['ufo_dead'],
            pos,
            duration,
            'player_bullets ufo',
            self.group
        )