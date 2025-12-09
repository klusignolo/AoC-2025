with open("input.txt", "r") as file:
    coordinates = [(int(coordinate.split(",")[0]), int(coordinate.split(",")[1])) for coordinate in file.read().splitlines()]
largest_area = 0
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i == j or j < i:
            continue
        coord_a = coordinates[i]
        coord_b = coordinates[j]
        rectangular_area = abs(coord_a[0] - coord_b[0] + 1) * abs(coord_a[1] - coord_b[1] + 1)
        if rectangular_area > largest_area:
            largest_area = rectangular_area
print(largest_area)