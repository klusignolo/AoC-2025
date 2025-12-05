with open("input.txt", "r") as f:
    data = f.read().split("\n\n")
    fresh_ranges = [(int(item.split("-")[0]), int(item.split("-")[1])) for item in data[0].splitlines()]
    available_ingredients = [int(item) for item in data[1].splitlines()]

fresh_ingredient_sum = 0
for ingredient in available_ingredients:
    for r in fresh_ranges:
        if r[0] <= ingredient <= r[1]:
            fresh_ingredient_sum += 1
            break
    else:
        print(f"Invalid ingredient found: {ingredient}")
print(fresh_ingredient_sum)