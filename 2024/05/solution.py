# Solution pour le jour 05 de l'Advent of Code 2024

with open("./2024/05/input.txt") as f: lines = [line.strip() for line in f.readlines()]

sep = lines.index("")
list1 = {}
for line in lines[:sep]:
    a, b = map(int, line.split('|'))
    list1.setdefault(a, []).append(b)
list2 = [list(map(int, line.split(","))) for line in lines[sep+1:]]

def correct(update):
    for i, page in enumerate(update):
        if set(list1[page]) & set(update[:i]): return False
    return True

def sort(update):
    sorted = [update[0]]
    for i in range(1, len(update)):
        inserted = False
        for j in range(len(sorted)):
            if update[i] in list1[sorted[j]]:
                sorted.insert(j, update[i])
                inserted = True
                break
        if not inserted: sorted.append(update[i])
    return sorted

res1 = 0
res2 = 0
for update in list2:
    if correct(update): res1 += update[len(update) // 2]
    else: 
        sorted = sort(update)
        res2 += sorted[len(sorted) // 2]

print("La première réponse est", res1)
print("La deuxième réponse est", res2)