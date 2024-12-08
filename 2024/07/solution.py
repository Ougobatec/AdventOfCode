# Solution pour le jour 07 de l'Advent of Code 2024

import itertools

with open("./2024/07/input.txt") as f: lines = [line.strip() for line in f.readlines()]

def calculate(nums, op, size, p2):
    ans = nums[0]
    for j in range(size):
        if op[j] == "0": ans += nums[j+1]
        elif op[j] == "1": ans *= nums[j+1]
        elif p2 and op[j] == "2": ans = int(f"{ans}{nums[j+1]}")
    return ans

res1 = 0
res2 = 0
for line in lines:
    val = int(line.split(":")[0])
    nums = list(map(int, line.split(":")[1].split()))
    size = len(nums) - 1
    for op in itertools.product("01", repeat=size):
        if calculate(nums, op, size, False) == val:
            res1 += val
            break
    for op in itertools.product("012", repeat=size):
        if calculate(nums, op, size, True) == val:
            res2 += val
            break

print("La première réponse est", res1)
print("La deuxième réponse est", res2)