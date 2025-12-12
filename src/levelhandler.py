from src.sprites import Player, GrassTile, DirtTile, SpikeTile

def parse_level(level_file_path):
    data = []
    with open(level_file_path, "r") as f:
        for line in f:
            line = line.strip("\n")
            chars = list(line)
            curr_line = []
            for char in chars:
                match char:
                    case ".":
                        curr_line.append(" ")
                    case "P":
                        curr_line.append(Player)
                    case "G":
                        curr_line.append(GrassTile)
                    case "D":
                        curr_line.append(DirtTile)
                    case "S":
                        curr_line.append(SpikeTile)
            data.append(curr_line)
    
    return data

if __name__ == "__main__":
    parse_level("./assets/levels/level1.txt")