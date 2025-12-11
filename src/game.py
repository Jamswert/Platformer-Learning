import pygame
from config.config import *

class Game:
    def __init__(self):
        pygame.init()

        # Timing and Runtime
        self.running = True
        self.clock = pygame.time.Clock()
        self.delta_time = 0.1
        self.framerate = FPS
        self.bg_color = BLACK

        pygame.display.set_caption(WINDOW_TITLE)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def tick(self):
        self.delta_time = self.clock.tick(self.framerate) / 1000
        self.delta_time = max(0.001, min(0.1, self.delta_time))


    def main(self):
        while self.running:
            self.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        
            self.screen.fill(self.bg_color)

            pygame.display.flip()

        pygame.quit()