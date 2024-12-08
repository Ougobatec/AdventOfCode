# Solution pour le jour 04 de l'Advent of Code 2024

with open("./2024/04/input.txt") as f: lines = f.readlines()

lines.append(" "*len(lines[0]))

directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
patterns = [('M', 'M', 'S', 'S'), ('M', 'S', 'M', 'S'), ('S', 'M', 'S', 'M'), ('S', 'S', 'M', 'M')]

res1 = 0
res2 = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'X':
            for di, dj in directions:
                try:
                    if (lines[i + di][j + dj] == 'M' and lines[i + 2 * di][j + 2 * dj] == 'A' and lines[i + 3 * di][j + 3 * dj] == 'S'): res1 += 1
                except: pass

        if lines[i][j] == 'A':
            for p in patterns:
                try:
                    if (lines[i-1][j-1] == p[0] and lines[i-1][j+1] == p[1] and lines[i+1][j-1] == p[2] and lines[i+1][j+1] == p[3]): res2 += 1
                except: pass

print("La première réponse est", res1)
print("La deuxième réponse est", res2)