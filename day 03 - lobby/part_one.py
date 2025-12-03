with open("input.txt") as f:
    battery_banks = f.read().splitlines()

joltage_total = 0
BATTERY_COUNT = 12
for battery_bank in battery_banks:
    batteries = [int(battery) for battery in list(battery_bank)]

    best_batteries = []
    left_index = 0
    for i in range(BATTERY_COUNT,0,-1):
        highest_joltage = max(batteries[left_index:len(batteries)-i+1])
        left_index = batteries.index(highest_joltage, left_index, len(batteries))+1
        best_batteries.append(highest_joltage)
    joltage_total += int("".join(map(str, best_batteries)))
print(joltage_total)