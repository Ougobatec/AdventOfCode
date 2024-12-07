# Solution pour le jour 07 de l'Advent of Code 2024

import itertools

with open("input.txt") as f: lines = f.readlines()

def evaluate(nums, ops, size, p2):
    ans = nums[0]
    for j in range(size):
        op = ops[j]
        if op == "0": ans += nums[j+1]
        elif op == "1": ans *= nums[j+1]
        elif p2 and op == "2": ans = int(f"{ans}{nums[j+1]}")
    return ans

res1 = 0
res2 = 0
for line in lines:
    val = int(line.split(":")[0])
    nums = list(map(int, line.split(":")[1].strip().split()))
    size = len(nums) - 1

    for ops in itertools.product("01", repeat=size):
        if evaluate(nums, ops, size, False) == val:
            res1 += val
            break

    for ops in itertools.product("012", repeat=size):
        if evaluate(nums, ops, size, True) == val:
            res2 += val
            break

print("La première réponse est", res1)
print("La deuxième réponse est", res2)