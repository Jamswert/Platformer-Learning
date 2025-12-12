import pygame
from config.config import *
from src.sprites import Player, GrassTile, DirtTile, SpikeTile
from src.levelhandler import parse_level

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
        
        level_data = parse_level("./assets/levels/level1.txt")
        
        self.player = None
        for row_index, row in enumerate(level_data):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_WIDTH
                y = row_index * TILE_HEIGHT
                
                if cell == Player:
                    self.player = Player(x, y)
                    self.player.tile_sprites = self.tile_sprites
                    self.all_sprites.add(self.player)
                elif cell == GrassTile:
                    new_tile = GrassTile(x, y)
                    self.tile_sprites.add(new_tile)
                    self.all_sprites.add(new_tile)
                elif cell == DirtTile:
                    new_tile = DirtTile(x, y)
                    self.tile_sprites.add(new_tile)
                    self.all_sprites.add(new_tile)
                elif cell == SpikeTile:
                    new_tile = SpikeTile(x, y)
                    self.tile_sprites.add(new_tile)
                    self.all_sprites.add(new_tile)
        
        if self.player is None:
            self.player = Player(60, 450)
            self.player.tile_sprites = self.tile_sprites
            self.all_sprites.add(self.player)

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
            debug_text = DEBUG_FONT.render(f"FPS: {self.clock.get_fps():.0f}, Jumps Used: {self.player.current_jumps}, Max Jumps: {self.player.max_jump_count}", antialias=True, color=WHITE)
            self.screen.blit(debug_text, (10, 10))

            pygame.display.flip()

        pygame.quit()