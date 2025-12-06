with open("input.txt", "r") as file:
    lines = [line.split()for line in file.read().splitlines()]
top_numbers = [int(x) for x in lines[0]]
middle_numbers1 = [int(x) for x in lines[1]]
middle_numbers2 = [int(x) for x in lines[2]]
bottom_numbers = [int(x) for x in lines[3]]
operators = lines[4]
problems = [(top_numbers[i], middle_numbers1[i], middle_numbers2[i], bottom_numbers[i], operators[i]) for i in range(len(lines[0]))]
total_sum = 0
for problem in problems:
    top, middle1, middle2, bottom, operator = problem
    if operator == "+":
        total_sum += top + middle1 + middle2 + bottom
    elif operator == "*":
        total_sum += top * middle1 * middle2 * bottom
print(total_sum)