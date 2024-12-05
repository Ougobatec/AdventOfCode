# Solution pour le jour 01 de l'Advent of Code 2024

with open("input.txt") as f: lines = f.readlines()

list1 = [list(map(int, line.strip().split()))[0] for line in lines]
list2 = [list(map(int, line.strip().split()))[1] for line in lines]

list1.sort()
list2.sort()

res1 = sum(abs(list1[i] - list2[i]) for i in range(len(list1)))
print("La première réponse est", res1)

res2 = sum(i * list2.count(i) for i in list1)
print("La deuxième réponse est", res2)