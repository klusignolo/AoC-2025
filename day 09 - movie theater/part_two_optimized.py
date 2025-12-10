with open("input.txt", "r") as file:
    POLYGON = [(int(coordinate.split(",")[0]), int(coordinate.split(",")[1])) for coordinate in file.read().splitlines()]


VERTICAL_LINES = []
HORIZONTAL_LINES = []

for i, coord in enumerate(POLYGON):
    if i + 1 < len(POLYGON):
        next_coord = POLYGON[i + 1]
    else:
        next_coord = POLYGON[0]  # wrap around to the first coordinate
        
    if coord[1] == next_coord[1]:  # same y-coordinate, horizontal line
        HORIZONTAL_LINES.append((coord, next_coord))
    if coord[0] == next_coord[0]:  # same x-coordinate, vertical line
        VERTICAL_LINES.append((coord, next_coord))

def is_in_polygon(point: tuple[int,int]) -> bool:
    x,y = point
    for horizontal_line in HORIZONTAL_LINES:
        x1,y1 = horizontal_line[0]
        x2 = horizontal_line[1][0]
        if y != y1: 
            continue
        else:
            left_x = min(x1,x2)
            right_x = max(x1,x2)
            if x <= right_x and x >= left_x:
                return True, right_x # point falls on a horizontal line

    intersections = []
    for vertical_line in VERTICAL_LINES:
        x1,y1 = vertical_line[0]
        y2 = vertical_line[1][1]
        if x > x1: 
            continue # point falls to the right of the vertical line
        y_top = max(y1,y2)
        y_bottom = min(y1,y2)
        if x == x1 and y <= y_top and y >= y_bottom: 
            return True, x # point falls on a vertical line
        elif y <= y_top and y > y_bottom:
            intersections.append(x1) # point falls to the left of the vertical line
    return len(intersections) % 2 == 1, x if len(intersections) == 0 else min(intersections)

largest_area = 0
area_points = None
points_to_count = len(POLYGON)
points_counted = 0
for point_a in POLYGON:
    points_counted += 1
    print(f"Counted {points_counted}/{points_to_count}")
    # For each point, compare against all polygon points to the right.
    other_points = filter(lambda x: x[0] >= point_a[0], POLYGON)
    for point_b in other_points:
        x1,y1 = point_a
        x2,y2 = point_b
        potential_rectangle_area = abs((x2 - x1 + 1)*(y2 - y1 + 1))
        # Determine if a rectangle can be formed that is larger than the current largest rectangle
        if largest_area >= potential_rectangle_area: continue

        is_valid_rectangle = True
        for y in range(min(y1,y2), max(y1,y2)+1):
            if not is_valid_rectangle: break
            x = x1
            while x < x2+1: 
                if not is_valid_rectangle: break
                is_inside, next_x = is_in_polygon((x,y))
                if not is_inside:
                    is_valid_rectangle = False
                    continue
                else:
                    x = next_x + 1
        if is_valid_rectangle:
            largest_area = potential_rectangle_area
            area_points = point_a, point_b
print(largest_area)
# 10622324 too low
# 30872120 too low :(((