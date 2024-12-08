# Solution pour le jour 08 de l'Advent of Code 2024

with open("./2024/08/input.txt") as f: lines = [line.strip() for line in f.readlines()]

freq = {}
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char != ".":
            freq.setdefault(char, []).append((x, y))

res1 = set()
res2 = set()
for i in freq:
    for a in freq[i]:
        for b in freq[i]:
            if a != b:
                vect = (a[0] - b[0], a[1] - b[1])
                for n in range(len(lines)):
                    p1 = (a[0] + n*vect[0], a[1] + n*vect[1])
                    p2 = (b[0] - n*vect[0], b[1] - n*vect[1])
                    for p in (p1, p2):
                        if 0 <= p[0] < len(lines) and 0 <= p[1] < len(lines[0]):
                            if n == 1: res1.add(p)
                            res2.add(p)

print("La première réponse est", len(res1))
print("La deuxième réponse est", len(res2))