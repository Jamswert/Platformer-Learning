import pygame
from config.config import *

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_source, x, y, speed):
        super().__init__()
        if isinstance(image_source, str):
            self.image = pygame.image.load(image_source).convert_alpha()
        else:
            self.image = image_source
        
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = speed

    def update(self, delta_time):
        pass

class Player(GameSprite):
    def __init__(self, x, y):
        super().__init__("assets/sprites/ivan.png", x, y, PLAYER_SPEED)
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.lives = PLAYER_LIVES

