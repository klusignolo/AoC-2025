import re
with open("input.txt", "r") as file:
    lines = file.read().splitlines()
CURRENT_MAX_PATH = float('inf')
STARTING_MAX_PATH = float('inf')
class JoltagePath:
    def __init__(self, joltage: list[int], parent=None) -> None:
        self.parent = parent
        self.joltage = joltage
        self.length = parent.length + 1 if parent is not None else 0

    def is_solved(self) -> bool:
        return all(joltage == 0 for joltage in self.joltage)
    def is_valid(self) -> bool:
        if not all(joltage >= 0 for joltage in self.joltage):
            return False
        
        global CURRENT_MAX_PATH

        minimum_remaining_move_count = max(self.joltage)
        maximum_allowable_move_count = CURRENT_MAX_PATH - self.length - 1
        if minimum_remaining_move_count > maximum_allowable_move_count:
            return False
        return True
    
def apply_button_press(input_joltage: list[int], button: list[int]) -> list[int]:
    new_joltages = input_joltage.copy()
    for index in button:
        new_joltages[index] -= 1
    return new_joltages

def button_value(input_joltage: list[int], button: list[int]) -> int:
    value = 0
    for index in button:
        if input_joltage[index] == 0:
            return 0
        value += input_joltage[index]
    return value

def get_smallest_path(input_path: JoltagePath, buttons: list[list[int]]) -> list[list[int]]:
    global CURRENT_MAX_PATH
    global STARTING_MAX_PATH
    if input_path.length >= CURRENT_MAX_PATH-1:
        return float('inf')
    
    next_paths = []
    buttons.sort(key=lambda x: -button_value(input_path.joltage, x))
        # check how far we are from max path.
        # If the top button score * remaining moves is less than the remaining joltage, we can prune

    
    for button in buttons:
        new_joltage = apply_button_press(input_path.joltage, button)
        next_path = JoltagePath(new_joltage, input_path)
        if next_path.is_solved():
            CURRENT_MAX_PATH = min(CURRENT_MAX_PATH, next_path.length)
            print(f"New MAX PATH: {CURRENT_MAX_PATH}")
            return next_path.length
        if next_path.is_valid():
            next_paths.append(next_path)

    if len(next_paths) == 0:
        return float('inf')
    return min(get_smallest_path(path, buttons) for path in next_paths)

class Machine:
    def __init__(self, buttons: list[int], joltages: list[int]) -> None:
        self.buttons = sorted(buttons, reverse=True)
        self.joltages = joltages.copy()
    
    def solve(self) -> int:
        global STARTING_MAX_PATH
        global CURRENT_MAX_PATH
        STARTING_MAX_PATH = sum(self.joltages)
        CURRENT_MAX_PATH = STARTING_MAX_PATH
        initial_path = JoltagePath(self.joltages)
        return get_smallest_path(initial_path, self.buttons)


machines: list[Machine] = []
for line in lines:
    buttons_str = re.findall(r"\((.*?)\)", line)
    buttons = []
    for button_str in buttons_str:
        buttons.append([int(x) for x in button_str.split(",")])
    buttons.sort(key=lambda x: -len(x))
    joltages = [int(x) for x in line.split("{")[1].strip("}").split(",")]
    machines.append(Machine(buttons, joltages))
answer = 0
current_machine_index = 0
for machine in machines:
    lowest_number_of_moves = machine.solve()
    print(f"Machine {current_machine_index}/{len(machines)} solved: {lowest_number_of_moves} moves")
    answer += lowest_number_of_moves
    current_machine_index += 1
print(answer)
# 16444 too low :(((())))