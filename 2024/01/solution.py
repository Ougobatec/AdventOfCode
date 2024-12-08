# Solution pour le jour 01 de l'Advent of Code 2024

with open("./2024/01/input.txt") as f: lines = [line.strip() for line in f.readlines()]

list1 = [list(map(int, line.split()))[0] for line in lines]
list2 = [list(map(int, line.split()))[1] for line in lines]

list1.sort()
list2.sort()

res1 = sum(abs(list1[i] - list2[i]) for i in range(len(list1)))
print("La première réponse est", res1)

res2 = sum(i * list2.count(i) for i in list1)
print("La deuxième réponse est", res2)