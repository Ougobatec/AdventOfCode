# Solution pour le jour 01 de l'Advent of Code 2024

with open('input.txt') as f: lines = f.readlines()

list1 = []
list2 = []
for line in lines:
    elements = list(map(int, line.strip().split()))
    list1.append(elements[0])
    list2.append(elements[1])

list1.sort()
list2.sort()

sum = 0
for i in range(len(list1)): sum += abs(list1[i] - list2[i])

print("La première réponse est", sum)


sum = 0
for i in list1:
    count = list2.count(i)
    sum += i*count

print("La deuxième réponse est", sum)