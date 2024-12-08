# Solution pour le jour 02 de l'Advent of Code 2024

with open("./2024/02/input.txt") as f: lines = [line.strip() for line in f.readlines()]

reports = [list(map(int, line.split())) for line in lines]

def test(levels):
    if levels == sorted(levels) or levels == sorted(levels, reverse=True):
        for i in range(len(levels) - 1):
            if not (1 <= abs(levels[i] - levels[i+1]) <= 3): return False
        return True

res1 = sum(1 for report in reports if test(report))
print("La première réponse est", res1)

res2 = sum(1 for report in reports if test(report) or any(test(report[:i] + report[i + 1:]) for i in range(len(report))))
print("La deuxième réponse est", res2)