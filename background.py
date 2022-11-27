import pygame
import random
from pygame.locals import (
    RLEACCEL,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("Assets\Background\cloud.jpg").convert()
        self.surf = pygame.transform.scale(self.surf, (150,150))

        self.surf.set_colorkey((255,255,255), RLEACCEL)

        # RANDOMLY GENERATED STARTING POSITION
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )

    def update(self):
        self.rect.move_ip(-1, 0)
        if self.rect.right < 0:
            self.kill()
