with open("input.txt", "r") as f:
    data = f.read().split("\n\n")
    fresh_ranges = [[int(item.split("-")[0]), int(item.split("-")[1])] for item in data[0].splitlines()]
    available_ingredients = [int(item) for item in data[1].splitlines()]

fresh_ranges.sort(key=lambda x: x[0])
valid_ranges = [fresh_ranges[0]]
for i, fresh_range in enumerate(fresh_ranges[1:], start=1):
    valid_ranges.append(fresh_range)
    if valid_ranges[i-1][1] >= fresh_range[0]:
        valid_ranges[i-1][1] = fresh_range[0]-1
valid_ingredient_sum = 0
for valid_range in valid_ranges:
    valid_ingredient_sum += valid_range[1] - valid_range[0] + 1
print(f"Total number of fresh ingredients: {valid_ingredient_sum}")
# 312456880321056 too low