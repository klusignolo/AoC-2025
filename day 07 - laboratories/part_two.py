with open("input.txt", "r") as file:
    rows = file.read().splitlines()
TACHYON_GRID = [[char for char in row] for row in rows]

def get_next_positions(current_x: int, current_y: int) -> list[int]:
    next_pos = TACHYON_GRID[current_y][current_x]
    if next_pos == ".":
        return [current_x]
    else:
        return [current_x - 1, current_x + 1]

y_pos = 0
possibilities = 1
current_x_positions = {TACHYON_GRID[0].index("S"): 1}
GRID_COPY = TACHYON_GRID.copy()
while y_pos < len(TACHYON_GRID) - 1:
    y_pos += 1
    print(f"{y_pos}/{len(TACHYON_GRID)-1}")
    next_positions = []
    new_x_positions = {}
    for pos in current_x_positions.keys():
        nexts = get_next_positions(pos, y_pos)
        for next in nexts:
            beam_count = current_x_positions[pos]
            if next in new_x_positions:
                new_x_positions[next] += beam_count # another beam reaches here
            else:
                new_x_positions[next] = beam_count
    current_x_positions = new_x_positions
total_beams = sum(current_x_positions.values())
print(total_beams)