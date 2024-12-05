# Solution pour le jour 02 de l'Advent of Code 2024

with open('input.txt') as f: lines = f.readlines()

reports = []
for line in lines:
    elements = list(map(int, line.strip().split()))
    reports.append(elements)

def test(levels):
    if levels == sorted(levels) or levels == sorted(levels, reverse=True):
        for i in range(len(levels) - 1):
            if not (1 <= abs(levels[i] - levels[i+1]) <= 3): return False
        return True

sum = 0
for report in reports:
    if test(report): sum += 1

print("La première réponse est", sum)


sum = 0
for report in reports:
    safe = False
    if test(report): safe = True
    for i in range(len(report)):
        content = report[:i] + report[i + 1:]
        if test(content): safe = True
    if safe: sum += 1

print("La deuxième réponse est", sum)