from math import lcm
joltages = [7,5,12,7,2] # this must be represented in base 420
options = [[0,2,3,4],[2,3],[0,4],[0,1,2],[1,2,3,4],[7,5,12,7,2]]
base = lcm(*joltages)
target_base_integers = []
for option in options:
    builder = []
    for i in range(0, max(option)+1):
        builder.append("1") if i in option else builder.append("0")
    target_base_integers.append(int("".join(builder[::-1]),base))
            
# working with base 420
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
# so each slot is 420 ** 7, 420 **5
target = []
for i in range(1,len(joltages)+1):
    target.append(base**1)
for joltage in joltages:
    new_base = numberToBase(multiple**joltage, multiple)
    print(new_base)