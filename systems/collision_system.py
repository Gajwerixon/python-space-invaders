import pygame

from config import *

class CollisionSystem:
    """Collision System class"""
    def __init__(self, player, shield_blocks, player_bullets, 
                 alien_bullets, aliens, effect_system):
        self.player = player
        self.player_bullets = player_bullets

        self.aliens = aliens
        self.alien_bullets = alien_bullets

        self.shield_blocks = shield_blocks

        self.effect_system = effect_system

    def update(self):
        """Update collision system"""
        self.player_bullet_outside_play_area()
        self.player_bullets_aliens_collision()
        self.player_bullets_shield_collision()

        self.alien_bullet_outside_play_area()
        self.alien_bullet_player_collision()
        self.alien_bullet_shield_collision()

    def player_bullet_outside_play_area(self):
        """Player bullet hit play area top"""
        for bullet in self.player_bullets:
            if bullet.rect.top <= PLAY_AREA.top:
                bullet.kill()
                self.effect_system.spawn_player_bullet_miss_explosion(
                    bullet.rect.midtop,
                    0.25,
                )

    def player_bullets_aliens_collision(self):
        """Bullet and alien collision"""
        collision = pygame.sprite.groupcollide(
            self.player_bullets, 
            self.aliens, 
            True, 
            True
        )

        for _, aliens in collision.items():
            self.effect_system.player_bullets_aliens_fx(
                aliens[0].rect.center,
                0.25
            ) 

    def player_bullets_shield_collision(self):
        """Player bullet and shield collision"""
        collision = pygame.sprite.groupcollide(self.player_bullets, self.shield_blocks, True, True)
        for bullet, shields in collision.items():
            shields[0].damage_shield()
            self.effect_system.spaw_bullet_shield_explosion(
                bullet.rect.midtop,
                0.1
            ) 

    def alien_bullet_outside_play_area(self):
        """Alien bullet hit the play area bottom"""
        for bullet in self.alien_bullets:
            if bullet.rect.bottom >= PLAY_AREA.bottom:
                bullet.kill()
                self.effect_system.spawn_alien_bullet_miss_explosion(
                    bullet.rect.midbottom,
                    0.25,
                )

    def alien_bullet_player_collision(self):
        """Alien bullet and player collision"""
        collision = pygame.sprite.groupcollide(self.player, self.alien_bullets, True, True)
        for player, _ in collision.items():
            self.effect_system.spawn_player_explosion(
                player.rect.center,
                1.5,
                0.125,
            )

    def alien_bullet_shield_collision(self):
        """Alien bullet and shield collision"""
        collision = pygame.sprite.groupcollide(self.alien_bullets, self.shield_blocks, True, True)
        for bullet, shields in collision.items():
            shields[0].damage_shield()
            self.effect_system.spawn_alien_bullet_shield_explosion(
                bullet.rect.midbottom,
                0.1
            )