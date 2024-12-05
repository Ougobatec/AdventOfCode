# Solution pour le jour 04 de l'Advent of Code 2024

with open('input.txt') as f: lines = f.readlines()

lines.append(" "*len(lines[0]))

sum1 = 0
sum2 = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'X':
            try:
                if lines[i][j-1] == 'M' and lines[i][j-2] == 'A' and lines[i][j-3] == 'S': sum1 += 1
            except: next
            try:
                if lines[i][j+1] == 'M' and lines[i][j+2] == 'A' and lines[i][j+3] == 'S': sum1 += 1
            except: next
            try:
                if lines[i-1][j] == 'M' and lines[i-2][j] == 'A' and lines[i-3][j] == 'S': sum1 += 1
            except: next
            try:
                if lines[i+1][j] == 'M' and lines[i+2][j] == 'A' and lines[i+3][j] == 'S': sum1 += 1
            except: next
            try:
                if lines[i-1][j-1] == 'M' and lines[i-2][j-2] == 'A' and lines[i-3][j-3] == 'S': sum1 += 1
            except: next
            try:
                if lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S': sum1 += 1
            except: next
            try:
                if lines[i-1][j+1] == 'M' and lines[i-2][j+2] == 'A' and lines[i-3][j+3] == 'S': sum1 += 1
            except: next
            try:
                if lines[i+1][j-1] == 'M' and lines[i+2][j-2] == 'A' and lines[i+3][j-3] == 'S': sum1 += 1
            except: next

        if lines[i][j] == 'A':
            try:
                if lines[i-1][j-1] == 'M' and lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S' and lines[i+1][j+1] == 'S': sum2 += 1
            except: next
            try:
                if lines[i-1][j-1] == 'M' and lines[i-1][j+1] == 'S' and lines[i+1][j-1] == 'M' and lines[i+1][j+1] == 'S': sum2 += 1
            except: next
            try:
                if lines[i-1][j-1] == 'S' and lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S' and lines[i+1][j+1] == 'M': sum2 += 1
            except: next
            try:
                if lines[i-1][j-1] == 'S' and lines[i-1][j+1] == 'S' and lines[i+1][j-1] == 'M' and lines[i+1][j+1] == 'M': sum2 += 1
            except: next

print("La première réponse est", sum1)
print("La deuxième réponse est", sum2)