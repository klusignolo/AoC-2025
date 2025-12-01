with open("input.txt", "r") as file_contents:
    instructions = file_contents.readlines()

DIAL_SIZE = 100
current_number = 50
current_direction = "R"
password = 0

for instruction in instructions:
    number_of_clicks = int(instruction[1:])
    turn_direction = instruction[0]

    did_swap_directions = turn_direction != current_direction
    current_direction = turn_direction

    if current_number > 0 and did_swap_directions:
        current_number = DIAL_SIZE - current_number

    total_clicks = current_number + number_of_clicks
    count_of_pass_zero = int(total_clicks / DIAL_SIZE)
    password += count_of_pass_zero

    current_number = total_clicks % DIAL_SIZE

print(password)
