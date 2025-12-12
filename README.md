# Platformer Learning (Pygame)

A small OOP (Object Oriented Programming) pygame platformer that should help me learn how to make games properly in pygame.

I'm using a setup with a main entry point and then packages with classes and modules when needed.

## Project structure
- `main.py` — the entry point for the project.
- `src/game.py` — `Game` class: Handles the main game
- `src/sprites.py` - Holds classes for rhe creation of a sprite and also the sprite logic such as player movement.
- `config/config.py` — window settings (size, title, FPS) and shared colors.

## Prerequisites
- Python 3.10+ (other 3.x likely fine)
- `pygame` installed (`pip install pygame`)

## Level Editor
- This is a work in progress, it takes in text files and parses it.
- These need to be in the format of a 37 columns long by 20 rows tall text file.
- Types:
    - `G` - `GrassTile` location
    - `P` - `Player` spawn location
    - `S` - `SpikeTile` location
    - `D` - `DirtTile` location
    - `.` - `None`

## Next steps / ideas to extend
- Add a player sprite with movement and gravity.
- Implement a basic tile map and platforms.
- Learn how to make a level editor / handler (text files?)
- Handle input for jumping and horizontal movement.
- Track delta time (`self.delta_time`) to make movement frame-rate independent.
- Add simple UI (FPS display) and pause/quit menu.

