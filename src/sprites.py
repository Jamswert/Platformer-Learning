import pygame
from config.config import *
from src.soundhandler import load_sound

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
        # Recreate rect with correct size after scaling
        self.rect = self.image.get_rect(topleft=(x, y))
        self.lives = PLAYER_LIVES
        self.direction_x = 0
        self.velocity_y = 0
        self.spawn_x = x
        self.spawn_y = y

        self.on_ground = False
        self.tile_sprites = None

        self.death_sound = load_sound("assets/sounds/sfx/death.wav", volume=300)
        self.jump_sound = load_sound("assets/sounds/sfx/jump.wav", volume=100)
        self.jump_held = False  # prevents consuming multiple jumps while key is held
        
        self.max_jump_count = PLAYER_JUMP_COUNT
        self.current_jumps = 0
    
    def handle_input(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction_x = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction_x = 1
        else:
            self.direction_x = 0
        
        jump_pressed = keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]

        # Edge-detect jump so holding the key doesn't chain-fire jumps
        if jump_pressed and not self.jump_held and self.current_jumps < self.max_jump_count:
            self.velocity_y = JUMP_STRENGTH
            self.on_ground = False
            self.current_jumps += 1
            self.jump_sound.play()
            self.jump_held = True
        elif not jump_pressed:
            self.jump_held = False

    def update(self, delta_time):
        # Store previous position for collision detection
        prev_x = self.rect.x
        prev_y = self.rect.y
        
        # Apply horizontal movement
        self.rect.x += self.direction_x * self.speed * delta_time

        # Check horizontal collisions (exclude spike tiles)
        if self.tile_sprites:
            horizontal_collisions = pygame.sprite.spritecollide(self, self.tile_sprites, False)
            for tile in horizontal_collisions:
                # Skip spike tiles - they don't block movement, they kill
                if isinstance(tile, SpikeTile):
                    continue
                if self.direction_x > 0:
                    self.rect.right = tile.rect.left
                elif self.direction_x < 0:
                    self.rect.left = tile.rect.right
        
        # Apply gravity and vertical movement
        self.velocity_y += GRAVITY * delta_time
        self.rect.y += self.velocity_y * delta_time

        # Check for spike tile collisions (death) - check before normal collision handling
        if self.tile_sprites:
            spike_collisions = pygame.sprite.spritecollide(self, self.tile_sprites, False)
            for tile in spike_collisions:
                if isinstance(tile, SpikeTile):
                    self.death_sound.play()
                    self.respawn()
                    return  # Exit early to prevent further collision handling

        # Check vertical collisions (exclude spike tiles)
        self.on_ground = False
        if self.tile_sprites:
            # Get all tiles the player is currently colliding with
            vertical_collisions = pygame.sprite.spritecollide(self, self.tile_sprites, False)
            
            for tile in vertical_collisions:
                # Skip spike tiles - they don't block movement, they kill
                if isinstance(tile, SpikeTile):
                    continue
                    
                # Calculate previous bottom position
                prev_bottom = prev_y + self.rect.height
                
                # Determine which side the player is overlapping from
                overlap_from_top = self.rect.bottom - tile.rect.top
                overlap_from_bottom = tile.rect.bottom - self.rect.top
                
                # Ground collision: player is falling (or stationary) and overlapping tile from above
                if self.velocity_y >= 0:
                    # Check if player's bottom crossed into the tile
                    if self.rect.bottom > tile.rect.top:
                        # Make sure player was above tile before movement
                        if prev_bottom <= tile.rect.top:
                            self.rect.bottom = tile.rect.top
                            self.velocity_y = 0
                            self.on_ground = True
                            self.current_jumps = 0
                            break
                        # If already inside, push up if more overlap from top
                        elif overlap_from_top > overlap_from_bottom:
                            self.rect.bottom = tile.rect.top
                            self.velocity_y = 0
                            self.on_ground = True
                            break
                
                # Ceiling collision: player is moving up and overlapping tile from below
                elif self.velocity_y < 0:
                    # Check if player's top crossed into the tile
                    if self.rect.top < tile.rect.bottom:
                        # Make sure player was below tile before movement
                        if prev_y >= tile.rect.bottom:
                            self.rect.top = tile.rect.bottom
                            self.velocity_y = 0
                            break
                        # If already inside, push down if more overlap from bottom
                        elif overlap_from_bottom > overlap_from_top:
                            self.rect.top = tile.rect.bottom
                            self.velocity_y = 0
                            break

        # Screen boundary checks
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
    
    def respawn(self):
        """Respawn the player at their spawn position"""
        self.rect.x = self.spawn_x
        self.rect.y = self.spawn_y
        self.velocity_y = 0
        self.current_jumps = 0

class GrassTile(GameSprite):
    def __init__(self, x, y):
        super().__init__("assets/sprites/grass_tile.png", x, y, 0)
        self.image = pygame.transform.scale(self.image, (TILE_WIDTH, TILE_HEIGHT))
        # Recreate rect with correct size after scaling
        self.rect = self.image.get_rect(topleft=(x, y))

class DirtTile(GameSprite):
    def __init__(self, x, y):
        super().__init__("assets/sprites/dirt_tile.png", x, y, 0)
        self.image = pygame.transform.scale(self.image, (TILE_WIDTH, TILE_HEIGHT))
        # Recreate rect with correct size after scaling
        self.rect = self.image.get_rect(topleft=(x, y))

class SpikeTile(GameSprite):
    def __init__(self, x, y):
        super().__init__("assets/sprites/spike.png", x, y, 0)
        self.image = pygame.transform.scale(self.image, (TILE_WIDTH, TILE_HEIGHT))
        # Recreate rect with correct size after scaling
        self.rect = self.image.get_rect(topleft=(x, y))