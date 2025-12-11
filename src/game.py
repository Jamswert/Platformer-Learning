import pygame
from config.config import *
from src.sprites import Player

class Game:
    def __init__(self):
        pygame.init()

        # Timing and Runtime
        self.running = True
        self.clock = pygame.time.Clock()
        self.delta_time = 0.1
        self.framerate = FPS
        self.bg_color = BG_COLOR

        pygame.display.set_caption(WINDOW_TITLE)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.all_sprites = pygame.sprite.Group()
        
        self.player = Player(60, 500)
        self.all_sprites.add(self.player)

    def tick(self):
        self.delta_time = self.clock.tick(self.framerate) / 1000
        self.delta_time = max(0.001, min(0.1, self.delta_time))

    def main(self):
        while self.running:
            self.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.all_sprites.update(self.delta_time)

            self.screen.fill(self.bg_color)
            self.all_sprites.draw(self.screen)

            pygame.display.flip()

        pygame.quit()