# Platformer Learning (Pygame)

A small OOP (Object Oriented Programming) pygame platformer that should help me learn how to make games properly in pygame.

I'm using a setup with a main entry point and then packages with classes and modules when needed.

## Features

- **Player Movement**: Smooth horizontal movement with gravity and physics
- **Multiple Jumps**: Double jump system (configurable jump count)
- **Level System**: Text-based level files parsed and rendered
- **Collision Detection**: Full collision handling for platforms, walls, and ceilings
- **Hazard System**: Spike tiles that kill the player and trigger respawn
- **Sound System**: Background music and sound effects (jump, death)
- **Debug UI**: Real-time FPS and jump counter display
- **Frame-Rate Independent**: Delta time based movement for consistent gameplay

## Project structure
- `main.py` — the entry point for the project.
- `src/game.py` — `Game` class: Handles the main game loop, rendering, and input
- `src/sprites.py` — Sprite classes including `Player`, `GrassTile`, `DirtTile`, and `SpikeTile` with collision logic
- `src/levelhandler.py` — Level parsing from text files
- `src/soundhandler.py` — Sound and music management (`SoundEffect` and `Music` classes)
- `config/config.py` — Window settings (size, title, FPS), game constants, and shared colors

## Prerequisites
- Python 3.10+ (other 3.x likely fine)
- `pygame` installed (`pip install pygame`)

## Controls
- **Movement**: `A`/`D` or `Left Arrow`/`Right Arrow` keys
- **Jump**: `Space`, `W`, or `Up Arrow` keys
- **Quit**: Close window or `Alt+F4`

## Level Format
Levels are stored as text files in `assets/levels/` and parsed automatically.

- **Format**: Text files with characters representing tile types
- **Tile Types**:
    - `G` - `GrassTile` (platform)
    - `D` - `DirtTile` (platform)
    - `S` - `SpikeTile` (hazard - kills player on contact)
    - `P` - `Player` spawn location
    - `.` - Empty space

Example level file: `assets/levels/level1.txt`

## Sound System
- **Background Music**: Looping music tracks in `assets/sounds/music/`
- **Sound Effects**: Jump and death sounds in `assets/sounds/sfx/`
- Volume controls available in `soundhandler.py`

## Next steps / ideas to extend
- Add more level files
- Implement collectibles or power-ups
- Add enemy AI
- Create a main menu system
- Add pause functionality
- Implement scoring system
- Add particle effects
- Create more tile types and hazards

