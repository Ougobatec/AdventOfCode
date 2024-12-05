# Solution pour le jour 03 de l'Advent of Code 2024

import re

with open('input.txt') as f: text = f.read()

template = r"mul\((\d{1,3}),(\d{1,3})\)"
res = re.findall(template, text)

sum = 0
for val in res: sum += int(val[0]) * int(val[1])

print("La première réponse est", sum)


template = r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))"
res = re.findall(template, text)

sum = 0
test = True
for i in res:
    if i[0] and test:
        values = i[0][4:][:-1].split(",")
        sum += int(values[0]) * int(values[1])
    if i[1]: test = True
    if i[2]: test = False

print("La deuxième réponse est", sum)