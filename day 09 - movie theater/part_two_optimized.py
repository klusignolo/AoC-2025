with open("input.txt", "r") as file:
    POLYGON = [(int(coordinate.split(",")[0]), int(coordinate.split(",")[1])) for coordinate in file.read().splitlines()]

is_in_polygon_cache = []
is_not_in_polygon_cache = []

def is_on_segment(p_x, p_y, a_x, a_y, b_x, b_y):
    cross_product = (p_y - a_y) * (b_x - a_x) - (b_y - a_y) * (p_x - a_x)
    if abs(cross_product) > 1e-9:
        return False
    
    is_x_in_box = (min(a_x, b_x) <= p_x <= max(a_x, b_x))
    is_y_in_box = (min(a_y, b_y) <= p_y <= max(a_y, b_y))
    
    return is_x_in_box and is_y_in_box

def is_in_polygon(point: tuple[int,int]):
    if point in is_in_polygon_cache:
        return True
    if point in is_not_in_polygon_cache:
        return False
    x,y = point
    n = len(POLYGON)

    for i in range(n):
        x1, y1 = POLYGON[i]
        x2, y2 = POLYGON[(i + 1) % n]
        
        if is_on_segment(x, y, x1, y1, x2, y2):
            is_in_polygon_cache.append(point)
            return True
            
    # --- PART 2: Check for STRICTLY INSIDE (Optimized Ray Casting) ---
    intersection_count = 0
    for i in range(n):
        x1, y1 = POLYGON[i]
        x2, y2 = POLYGON[(i + 1) % n] 
        
        # 1. Check if the edge is vertical (x1 == x2)
        if x1 == x2:
            
            # The x-coordinate of the intersection is x1 (or x2)
            x_intersect = x1
            
            # 2. Check if the vertical edge is to the right of the test point
            if x_intersect > x:
                
                # 3. Check if the test point's y_p is strictly between the edge's y-coordinates.
                # This is the simplified straddling check that also handles the vertex rule:
                min_y = min(y1, y2)
                max_y = max(y1, y2)
                
                if min_y < y < max_y:
                    intersection_count += 1
                    
    # If the count is odd, the point is strictly inside.
    if intersection_count % 2 == 1:
        is_in_polygon_cache.append(point)
        return True
    else:
        is_not_in_polygon_cache.append(point)
        return False

largest_area = 0
area_points = None
points_to_count = len(POLYGON)
points_counted = 0
for point_a in POLYGON:
    points_counted += 1
    print(f"Counted {points_counted}/{points_to_count}")
    # For each point, compare against all polygon points to the right.
    for point_b in POLYGON:
        x_a,y_a = point_a
        x_b,y_b = point_b
        if min(x_a,x_b) == x_a:
            x1,y1 = point_a
            x2,y2 = point_b
        else:
            x1,y1 = point_b
            x2,y2 = point_a
        potential_rectangle_area = abs((x2 - x1 + 1)*(y2 - y1 + 1))
        # Determine if a rectangle can be formed that is larger than the current largest rectangle
        if largest_area >= potential_rectangle_area: continue
        is_valid_rectangle = True
        for y in range(min(y1,y2), max(y1,y2)+1):
            if not is_valid_rectangle: break
            x = x1
            while x < x2+1: 
                if not is_valid_rectangle: break
                if not is_in_polygon((x,y)):
                    is_valid_rectangle = False
                    continue
                else:
                    x += 1
        if is_valid_rectangle:
            largest_area = potential_rectangle_area
            area_points = point_a, point_b
print(largest_area)
# 10622324 too low
# 30872120 too low :(((
# 4749900512 too high