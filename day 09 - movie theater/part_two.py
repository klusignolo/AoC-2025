with open("input.txt", "r") as file:
    coordinates = [(int(coordinate.split(",")[0]), int(coordinate.split(",")[1])) for coordinate in file.read().splitlines()]


#loop through coordinates, turning them into a series of connections that represent straight lines.
#this could be pairs of coordinates that represent the start and end of each line segment.
#if we order them numerically by x and numerically by y,
#we can know which segments are directly adjacent/parallel to each other.
# we then just have to find the longest stretch of adjacent/parallel segments to find the largest rectangle.
horizontal_lines = []
vertical_lines = []

for i, coord in enumerate(coordinates):
    if i + 1 < len(coordinates):
        next_coord = coordinates[i + 1]
    else:
        next_coord = coordinates[0]  # wrap around to the first coordinate
        
    if coord[1] == next_coord[1]:  # same y-coordinate, horizontal line
        horizontal_lines.append((coord, next_coord))
    elif coord[0] == next_coord[0]:  # same x-coordinate, vertical line
        vertical_lines.append((coord, next_coord))