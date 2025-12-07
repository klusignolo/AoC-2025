with open("input.txt", "r") as file:
    rows = file.read().splitlines()
    tachyon_grid = [[char for char in row] for row in rows]

y_pos = 0
total_splits = 0
x_positions = set()
x_positions.add(tachyon_grid[0].index("S"))

while y_pos < len(tachyon_grid) - 1:
    y_pos += 1
    straight_x_positions = set()
    split_x_positions = set()
    for x in x_positions:
        next_pos = tachyon_grid[y_pos][x]
        if next_pos == ".":
            straight_x_positions.add(x)
        else: # split occurs
            total_splits += 1
            split_x_positions.add(x - 1)
            split_x_positions.add(x + 1)
    x_positions = straight_x_positions.union(split_x_positions)
print(total_splits)