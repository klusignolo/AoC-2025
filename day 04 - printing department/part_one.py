with open("input.txt", "r") as file:
    toilet_paper_rows = file.read().splitlines()
toilet_paper_grid = [list(row) for row in toilet_paper_rows]

total_available_toilet_papers = 0
for row_index, row in enumerate(toilet_paper_grid):
    for col_index, col in enumerate(row):
        if col == ".": continue
        left = row[col_index - 1] if col_index > 0 else None
        right = row[col_index + 1] if col_index < len(row) - 1 else None
        up = toilet_paper_grid[row_index - 1][col_index] if row_index > 0 else None
        down = toilet_paper_grid[row_index + 1][col_index] if row_index < len(toilet_paper_grid) - 1 else None
        up_left = toilet_paper_grid[row_index - 1][col_index - 1] if row_index > 0 and col_index > 0 else None
        up_right = toilet_paper_grid[row_index - 1][col_index + 1] if row_index > 0 and col_index < len(row) - 1 else None
        down_left = toilet_paper_grid[row_index + 1][col_index - 1] if row_index < len(toilet_paper_grid) - 1 and col_index > 0 else None
        down_right = toilet_paper_grid[row_index + 1][col_index + 1] if row_index < len(toilet_paper_grid) - 1 and col_index < len(row) - 1 else None

        total_toilet_papers_adjacent = 0
        if left and left == "@":
            total_toilet_papers_adjacent += 1
        if right and right == "@":
            total_toilet_papers_adjacent += 1
        if up and up == "@":
            total_toilet_papers_adjacent += 1
        if down and down == "@":
            total_toilet_papers_adjacent += 1
        if up_left and up_left == "@":  
            total_toilet_papers_adjacent += 1
        if up_right and up_right == "@":  
            total_toilet_papers_adjacent += 1
        if down_left and down_left == "@":  
            total_toilet_papers_adjacent += 1
        if down_right and down_right == "@":  
            total_toilet_papers_adjacent += 1
        if total_toilet_papers_adjacent < 4:
            total_available_toilet_papers += 1
        up, down, left, right, up_left, up_right, down_left, down_right = None, None, None, None, None, None, None, None
print(total_available_toilet_papers)