import pygame

from config import PLAY_AREA

class CollisionSystem:
    """Collision System class"""
    def __init__(self, groups, effect_system):
        self.groups = groups
        self.effect_system = effect_system
        self.events = []

    def update(self):
        """Update collision system"""
        # Player
        self.player_bullets_play_area_top_collision()
        self.player_bullets_aliens_collision()
        self.player_bullets_shield_blocks_collision()
        self.player_bullets_ufo_collision()

        # Aliens
        self.alien_line_blocks_collision()
        self.alien_bullets_player_collision()
        self.alien_bullets_shield_blocks_collision()
        self.alien_shield_blocks_collision()

        # Other
        self.player_bullets_alien_bullets_collision()

    # --- Player ---
    def player_bullets_play_area_top_collision(self):
        """Collision between player_bullets and PLAY_AREA top (miss)"""
        for bullet in self.groups['player_bullets']:
            if bullet.rect.top <= PLAY_AREA.top:
                bullet.kill()
                self.effect_system.player_bullets_miss_fx(
                    bullet.rect.midtop,
                    0.25,
                )

    def player_bullets_aliens_collision(self):
        """Collision between player_bullets and aliens"""
        collision = pygame.sprite.groupcollide(
            self.groups['player_bullets'], 
            self.groups['aliens'], 
            True, 
            True
        )

        for _, aliens in collision.items():
            self.effect_system.player_bullets_aliens_fx(
                aliens[0].rect.center,
                0.25
            )
            self.events.append(('ALIEN_DEAD', aliens[0].score))

    def player_bullets_shield_blocks_collision(self):
        """Collision between player_bullets and shield_blocks"""
        collision = pygame.sprite.groupcollide(self.groups['player_bullets'], self.groups['shields'], True, True)
        for bullet, shields in collision.items():
            shields[0].damage_shield('player')
            self.effect_system.player_bullets_shield_blocks_fx(
                bullet.rect.center,
                0.1
            ) 
            break
    
    def player_bullets_ufo_collision(self):
        """Collision between player_bullets and ufo"""
        collision = pygame.sprite.groupcollide(
            self.groups['player_bullets'],
            self.groups['ufo'],
            True,
            True
        )

        for _, ufo in collision.items():
            self.effect_system.player_bullets_ufo_fx(
                ufo[0].rect.center,
                0.5
            )
            self.events.append(('UFO_DEAD', ufo[0].score))

    def player_bullets_alien_bullets_collision(self):
        """Collision between player_bullets and alien_bullets"""
        collision = pygame.sprite.groupcollide(
            self.groups['player_bullets'], 
            self.groups['alien_bullets'],
            True, 
            True
        )

        for player_bullet, _ in collision.items():
            self.effect_system.player_bullets_alien_bullets_fx(
                player_bullet.rect.midtop,
                0.2,
            )

    # --- Aliens ---
    def alien_line_blocks_collision(self):
        """Collision between alien_bullets and line_blocks"""
        collision = pygame.sprite.groupcollide(self.groups['alien_bullets'], 
                                               self.groups['lines'],
                                               True, False)
        for _, line in collision.items():
            line[0].apply_damage()
            self.effect_system.alien_bullets_miss_fx(
                line[0].rect.midtop,
                0.25,
                )

    def alien_bullets_player_collision(self):
        """Collision between alien_bullets and player"""
        collision = pygame.sprite.groupcollide(self.groups['player'], self.groups['alien_bullets'], True, True)
        for player, _ in collision.items():
            self.effect_system.player_hit_fx(
                player.rect.center,
                1.5,
                0.125,
            )
            self.events.append(('PLAYER_DEAD',))

    def alien_bullets_shield_blocks_collision(self):
        """Collision between alien_bullets and shield_blocks"""
        collision = pygame.sprite.groupcollide(self.groups['alien_bullets'], self.groups['shields'], True, True)
        for bullet, shields in collision.items():
            shields[0].damage_shield('alien')
            self.effect_system.alien_bullet_shield_fx(
                bullet.rect.midbottom,
                0.1
            )

    def alien_shield_blocks_collision(self):
        """Collision between alien and shield"""
        collision = pygame.sprite.groupcollide(self.groups['aliens'], self.groups['shields'], False, False)
        for _, blocks in collision.items():
            blocks[0].damage_shield_alien()