from itertools import combinations
import re
with open("input.txt", "r") as file:
    lines = file.read().splitlines()
class Machine:
    def __init__(self, target: int, switches: list[int], joltages: list[int]) -> None:
        self.target = target
        self.switches = switches
        self.joltages = joltages

    def solve(self) -> int:
        valid_combinations = []
        combinations = self.get_combinations()
        for combination in combinations:
            result = 0
            for integer in combination:
                result ^= integer
            if result == self.target:
                valid_combinations.append(combination)
        return min([len(combination) for combination in valid_combinations]) if valid_combinations else -1

    def get_combinations(self) -> list[list[int]]:
        all_combinations = []
        for r in range(1, len(self.switches) + 1):
            all_combinations.extend(list(combinations(self.switches, r)))
        return all_combinations

machines: list[Machine] = []
for line in lines:
    target_str = line.split("]")[0].strip("[").replace(".","0").replace("#","1")
    target = int("".join(reversed(target_str)), 2)
    switches_str = re.findall(r"\((.*?)\)", line)
    switches = []
    for switch_str in switches_str:
        indices = [int(x) for x in switch_str.split(",")]
        switch = 0
        for i in indices:
            switch ^= 2**i
        switches.append(switch)
    joltages = [int(x) for x in line.split("{")[1].strip("}").split(",")]
    machines.append(Machine(target, switches, joltages))
lowest_number_of_moves = 0
for machine in machines:
    lowest_number_of_moves += machine.solve()
print(lowest_number_of_moves)