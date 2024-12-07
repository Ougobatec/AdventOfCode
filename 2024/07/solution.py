# Solution pour le jour 07 de l'Advent of Code 2024

with open("input.txt") as f: lines = f.readlines()

def ternary(n, size):
    if n == 0: ternary = '0'
    else:
        ternary = ''
        while n:
            ternary = str(n % 3) + ternary
            n //= 3
    return ternary.zfill(size)

res1 = 0
res2 = 0
for line in lines:
    val = int(line.split(":")[0])
    nums = [int(num) for num in line.split(":")[1].strip().split()]
    size = len(nums) - 1

    for i in range(2**size):
        op = f"{i:0{size}b}"
        ans = nums[0]
        for j in range(size):
            match op[j]:
                case "0": ans += nums[j+1]
                case "1": ans *= nums[j+1]
        if ans == val:
            res1 += val
            break
    
    for i in range(3**size):
        op = ternary(i, size)
        ans = nums[0]
        for j in range(size):
            match op[j]:
                case "0": ans += nums[j+1]
                case "1": ans *= nums[j+1]
                case "2": ans = int(f"{ans}{nums[j+1]}")
        if ans == val:
            res2 += val
            break

print("La première réponse est", res1)
print("La deuxième réponse est", res2)