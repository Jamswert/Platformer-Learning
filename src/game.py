import pygame
from config.config import *
from src.sprites import Player, GrassTile

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
        self.tile_sprites = pygame.sprite.Group()
        
        self.player = Player(60, 450)
        self.player.tile_sprites = self.tile_sprites
        self.all_sprites.add(self.player)

        for column in range(25):
            new_tile = GrassTile(0 + (TILE_WIDTH * column), 550)
            self.tile_sprites.add(new_tile)
            self.all_sprites.add(new_tile)

    def tick(self):
        self.delta_time = self.clock.tick(self.framerate) / 1000
        self.delta_time = max(0.001, min(0.1, self.delta_time))

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)

    def main(self):
        while self.running:
            self.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.handle_input()

            self.all_sprites.update(self.delta_time)

            self.screen.fill(self.bg_color)
            self.all_sprites.draw(self.screen)
            
            # Render and blit debug text
            debug_text = DEBUG_FONT.render(f"FPS: {self.clock.get_fps():.0f}", antialias=True, color=WHITE)
            self.screen.blit(debug_text, (10, 10))

            pygame.display.flip()

        pygame.quit()