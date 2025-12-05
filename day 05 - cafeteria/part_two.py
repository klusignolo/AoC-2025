with open("input.txt", "r") as f:
    data = f.read().split("\n\n")
    fresh_ranges = [[int(item.split("-")[0]), int(item.split("-")[1])] for item in data[0].splitlines()]
    available_ingredients = [int(item) for item in data[1].splitlines()]

fresh_ranges.sort(key=lambda x: (x[0], x[1]))
current_index = 0
valid_ranges = [[fresh_ranges[0][0], fresh_ranges[0][1]]]
for fresh_range in fresh_ranges:
    current_range = valid_ranges[current_index]

    # current range jumps ahead and does not modify current range
    if fresh_range[0] > current_range[1]:
        current_index += 1
        valid_ranges.append(fresh_range)
        continue

    # current range falls within existing range
    if fresh_range[1] > current_range[1]:
        current_range[1] = fresh_range[1]
    valid_ranges[current_index] = current_range

valid_ingredient_sum = 0
for valid_range in valid_ranges:
    valid_ingredient_sum += valid_range[1] - valid_range[0] + 1
print(f"Total number of fresh ingredients: {valid_ingredient_sum}")