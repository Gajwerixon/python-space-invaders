from entities.effect import Effect
from entities.animated_effect import AnimatedEffect

class EffectSystem:
    """Effect system class """
    def __init__(self, effect_assets, group):
        self.assets = effect_assets
        self.group = group

    def _create_effect(self, asset_key, pos, duration, name, anchor='center'):
        """Create basic effect"""
        return Effect(
            self.assets[asset_key],
            pos,
            duration,
            name,
            self.group,
            anchor=anchor
        )

    def _create_animated_effect(self, pos, full_duration, frame_duration, asset_key, name, anchor='center'):
        """Create animated effect"""
        return AnimatedEffect(
            self.assets[asset_key],
            pos,
            full_duration,
            frame_duration,
            name,
            self.group,
        )

    # --- Player ---
    def player_bullets_aliens_fx(self, pos, duration=0.125):
        """Spawn explosion between player_bullets and aliens"""
        self._create_effect('alien_explosion_fx', pos, duration, 'player_bullets_aliens_fx')
    
    def player_bullets_shield_blocks_fx(self, pos, duration=0.125):
        """Spawn explosion between player bullets and shield blocks"""
        self._create_effect('player_bullet_fx', pos, duration, 'player_bullets_shield_blocks')

    def player_bullets_miss_fx(self, pos, duration=0.125):
        """Spawn explosion after player bullets hit PLAY_AREA top"""
        self._create_effect('player_bullet_fx', pos, duration, 'player_bullets miss', anchor='midtop')

    def player_bullets_alien_bullets_fx(self, pos, duration=0.125):
        """Spawn explosion after player bullets hit alien bullets"""
        self._create_effect('player_bullet_fx', pos, duration, 'player_bullets_alien_bullets')
        self._create_effect('alien_bullet_fx', (pos[0], pos[1] - 20), duration, 'player_bullets_alien_bullets')

    def player_bullets_ufo_fx(self, pos, duration=0.25):
        """Spawn explosion after player_bullets hit ufo"""
        self._create_effect('ufo_dead', pos, duration, 'player_bullets ufo')

    # --- Aliens ---
    def alien_bullets_miss_fx(self, pos, duration=0.125):
        """Spawn explosion effect after alien bullets hit PLAY_AREA bottom"""
        self._create_effect('alien_bullet_fx', pos, duration, 'alien_bullets miss', anchor='midbottom')

    def alien_bullet_shield_fx(self, pos, duration=0.125):
        """Spaw explosion between alien bullets and shield blocks"""
        self._create_effect('alien_bullet_fx', pos, duration, 'alien_bullets shield_blocks')

    def alien_bullet_player_fx(self, pos, full_duration=1.5, frame_duration=0.125):
        """Spawn explosion AnimtedEffect after player was hit"""
        self._create_animated_effect(pos, full_duration, frame_duration, 'player_explosion', 'player_explosion')