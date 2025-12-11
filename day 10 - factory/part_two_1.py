from itertools import combinations
import re
with open("test_input.txt", "r") as file:
    lines = file.read().splitlines()

PRIMES = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
class Machine:
    def __init__(self, target: int, switches: list[int], joltages: list[int]) -> None:
        self.target = target
        self.switches = sorted(switches, reverse=True)
        self.joltages = joltages.copy()
        self.joltage_target = 1
        for i in range(len(joltages)):
            self.joltage_target *= PRIMES[i] ** joltages[i]


    def solve(self) -> int:
        buttton_count = 0
        previous_target = self.joltage_target
        while self.joltage_target > 1:
            print(self.joltage_target)
            for switch in self.switches:
                if self.joltage_target % switch == 0:
                    buttton_count += 1
                    self.joltage_target /= switch
            if self.joltage_target == previous_target:
                print("SHIT")
            else:
                previous_target = self.joltage_target
        return buttton_count

machines: list[Machine] = []
for line in lines:
    target_str = line.split("]")[0].strip("[").replace(".","0").replace("#","1")
    target = int("".join(reversed(target_str)), 2)
    switches_str = re.findall(r"\((.*?)\)", line)
    switches = []
    for switch_str in switches_str:
        indices = [int(x) for x in switch_str.split(",")]
        switch = 1
        for i in indices:
            switch *= PRIMES[i]
        switches.append(switch)
    joltages = [int(x) for x in line.split("{")[1].strip("}").split(",")]
    machines.append(Machine(target, switches, joltages))
lowest_number_of_moves = 0
for machine in machines:
    lowest_number_of_moves += machine.solve()
print(lowest_number_of_moves)