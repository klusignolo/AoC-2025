with open("test_input.txt") as f:
    battery_banks = f.read().splitlines()

joltage_total = 0
for battery_bank in battery_banks:
    batteries = [int(battery) for battery in list(battery_bank)]
    highest_joltage = max(batteries[:len(batteries)-1])
    highest_index = batteries.index(highest_joltage)
    second_highest_joltage = max(batteries[highest_index+1:])
    max_joltage = int(f"{highest_joltage}{second_highest_joltage}")
    joltage_total += max_joltage
print(joltage_total)    