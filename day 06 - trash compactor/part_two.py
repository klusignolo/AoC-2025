with open("input.txt", "r") as file:
    lines = file.read().splitlines()

padded_lines = [["" for _ in range(len(lines[0].split()))] for _ in range(len(lines))]
current_index = 0
padded_lines[4] = lines[4].split()
for i in range(len(lines[0])):
    a = lines[0][i]
    b = lines[1][i]
    c = lines[2][i]
    d = lines[3][i]
    if a == b == c == d == " ":
        current_index += 1
        # moving to next number
        continue
    if a == " ":
        padded_lines[0][current_index] += "0"
    else:
        padded_lines[0][current_index] += a
    if b == " ":
        padded_lines[1][current_index] += "0"
    else:
        padded_lines[1][current_index] += b
    if c == " ":
        padded_lines[2][current_index] += "0"
    else:
        padded_lines[2][current_index] += c
    if d == " ":
        padded_lines[3][current_index] += "0"
    else:
        padded_lines[3][current_index] += d
    
# top_numbers = [x for x in lines[0]]
# middle_numbers1 = [x for x in lines[1]]
# middle_numbers2 = [x for x in lines[2]]
# bottom_numbers = [x for x in lines[3]]
# operators = lines[4]
problems = [(padded_lines[0][i], padded_lines[1][i], padded_lines[2][i], padded_lines[3][i], padded_lines[4][i]) for i in range(len(padded_lines[0]))]
total_sum = 0
for problem in problems:
    prob_length = len(problem[0])
    numbers = ["" for _ in range(prob_length)]
    for i in range(prob_length-1, -1, -1):
        if problem[0][i] != "0":
            numbers[i] += problem[0][i]
        if problem[1][i] != "0":
            numbers[i] += problem[1][i]
        if problem[2][i] != "0":
            numbers[i] += problem[2][i]
        if problem[3][i] != "0":
            numbers[i] += problem[3][i]
    operator = problem[4]
    if operator == "+":
        for num in numbers:
            total_sum += int(num) if num != "" else 0
    elif operator == "*":
        product = 1
        for num in numbers:
            product *= int(num) if num != "" else 1
        total_sum += product
print(total_sum)