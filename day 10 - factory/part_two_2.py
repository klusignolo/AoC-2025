import re
with open("input.txt", "r") as file:
    lines = file.read().splitlines()

class Machine:
    def __init__(self, buttons: list[int], joltages: list[int]) -> None:
        self.buttons = sorted(buttons, reverse=True)
        self.joltages = joltages.copy()
        self.button_presses = []
        self.most_recent_unpressed_index = None


    def solve(self) -> int:
        joltage_total = sum(self.joltages)
        while joltage_total != 0:
            positive_sum = sum([joltage for joltage in self.joltages if joltage > 0])
            negative_sum = sum([abs(joltage) for joltage in self.joltages if joltage < 0])
            should_unpress_button = negative_sum >= positive_sum
            if should_unpress_button:
                index_to_unpress = self.get_least_valuable_button()
                self.unpress_button(index_to_unpress)
                self.most_recent_unpressed_index = index_to_unpress
            else:
                button_index = self.get_most_valuable_button()
                self.press_button(button_index)
            joltage_total = sum([abs(joltage) for joltage in self.joltages])
        self.prove_solution()
        return len(self.button_presses)
    
    def press_button(self, button_index:int):
        self.button_presses.append(button_index)
        for index in self.buttons[button_index]:
            self.joltages[index] -= 1

    def unpress_button(self, button_index:int):
        if button_index in self.button_presses:
            self.button_presses.remove(button_index)
        else:
            print("Shit, this doesn't work")
        for index in self.buttons[button_index]:
            self.joltages[index] += 1 

    
    def get_least_valuable_button(self):
        button_values = {i:0 for i in range(0,len(self.buttons))}
        for b_index, button in enumerate(self.buttons):
            for j_index in button:
                if self.joltages[j_index] < 0:
                    button_values[b_index] += self.joltages[j_index]
        if self.most_recent_unpressed_index is not None:
            del(button_values[self.most_recent_unpressed_index])
        return min(button_values, key=button_values.get)

    
    def get_most_valuable_button(self):
        button_values = {i:0 for i in range(0,len(self.buttons))}
        for b_index, button in enumerate(self.buttons):
            for j_index in button:
                if self.joltages[j_index] == 0:
                    button_values[b_index] = 0
                    break
                else:
                    button_values[b_index] += self.joltages[j_index]
        return max(button_values, key=button_values.get)

    def prove_solution(self):
        new_joltages = [0 for _ in range(len(self.joltages))]
        for b_index in self.button_presses:
            for j_index in self.buttons[b_index]:
                new_joltages[j_index] += 1
        print(new_joltages)

machines: list[Machine] = []
for line in lines:
    buttons_str = re.findall(r"\((.*?)\)", line)
    buttons = []
    for button_str in buttons_str:
        buttons.append([int(x) for x in button_str.split(",")])
    joltages = [int(x) for x in line.split("{")[1].strip("}").split(",")]
    machines.append(Machine(buttons, joltages))
lowest_number_of_moves = 0
for machine in machines:
    lowest_number_of_moves += machine.solve()
print(lowest_number_of_moves)
# 16444 too low :(((())))