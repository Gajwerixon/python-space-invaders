import pygame

class Ufo(pygame.sprite.Sprite):
    """Ufo class"""
    def __init__(self, image, pos, direction_x, speed, score, group):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(self.rect.center)

        self.direction_x = direction_x
        self.speed = speed

        self.score = score

    def movement(self, dt):
        """Movement"""
        self.pos.x += self.direction_x * self.speed * dt
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y