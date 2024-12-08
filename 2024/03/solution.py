# Solution pour le jour 03 de l'Advent of Code 2024

import re

with open("./2024/03/input.txt") as f: text = f.read()

find = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", text)
res1 = sum(int(val[0]) * int(val[1]) for val in find)
print("La première réponse est", res1)

find = re.findall(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))", text)
res2 = 0
test = True
for i in find:
    if i[0] and test:
        values = i[0][4:][:-1].split(",")
        res2 += int(values[0]) * int(values[1])
    if i[1]: test = True
    if i[2]: test = False
print("La deuxième réponse est", res2)