with open("input.txt") as f:
    battery_banks = f.read().splitlines()

joltage_total = 0
for battery_bank in battery_banks:
    batteries = [int(battery) for battery in list(battery_bank)]

    best_batteries = []
    left_bumper = 0
    for i in range(12,0,-1):
        # Can't look any further right than the remaining number of batteries to turn on
        right_bumper = len(batteries)-i+1 

        highest_joltage = max(batteries[left_bumper:right_bumper])
        best_batteries.append(highest_joltage)

        # Now can't look any further left than the battery we just picked
        left_bumper = batteries.index(highest_joltage, left_bumper, len(batteries)) + 1

    joltage_total += int("".join(map(str, best_batteries)))
print(joltage_total)