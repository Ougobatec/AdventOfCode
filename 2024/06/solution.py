# Solution pour le jour 06 de l'Advent of Code 2024

with open("./2024/06/input.txt") as f: lines = [list(line.strip()) for line in f.readlines()]

position = next((i, line.index("^")) for i, line in enumerate(lines) if "^" in line)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction = 0

def step(lines, position, direction, obstacle):
    pos, way = position, direction
    visited = {}
    while True:
        if pos in visited and way in visited[pos]: return True, visited
        visited.setdefault(pos, []).append(way)
        next = (pos[0] + directions[way][0], pos[1] + directions[way][1])
        if not (0 <= next[0] < len(lines) and 0 <= next[1] < len(lines[0])): return False, visited
        if obstacle and next == obstacle:
            way = (way + 1) % 4
            continue
        if lines[next[0]][next[1]] == "#": way = (way + 1) % 4
        else: pos = next

def test_obstacle(lines, position, direction):
    obstacles = set()
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if lines[x][y] == "#" or (x, y) == position: continue
            if step(lines, position, direction, (x, y))[0]: obstacles.add((x, y))
    return obstacles

res1 = len(step(lines, position, direction, False)[1])
print("La première réponse est", res1)

res2 = len(test_obstacle(lines, position, direction))
print("La deuxième réponse est", res2)