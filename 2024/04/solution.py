# Solution pour le jour 04 de l'Advent of Code 2024

file = open('input.txt')
text = file.readlines()

text.append(" "*len(text[0]))

sum1 = 0
sum2 = 0
for i in range(len(text)):
    for j in range(len(text[i])):
        if text[i][j] == 'X':
            try:
                if text[i][j-1] == 'M' and text[i][j-2] == 'A' and text[i][j-3] == 'S': sum1 += 1
            except: next
            try:
                if text[i][j+1] == 'M' and text[i][j+2] == 'A' and text[i][j+3] == 'S': sum1 += 1
            except: next
            try:
                if text[i-1][j] == 'M' and text[i-2][j] == 'A' and text[i-3][j] == 'S': sum1 += 1
            except: next
            try:
                if text[i+1][j] == 'M' and text[i+2][j] == 'A' and text[i+3][j] == 'S': sum1 += 1
            except: next
            try:
                if text[i-1][j-1] == 'M' and text[i-2][j-2] == 'A' and text[i-3][j-3] == 'S': sum1 += 1
            except: next
            try:
                if text[i+1][j+1] == 'M' and text[i+2][j+2] == 'A' and text[i+3][j+3] == 'S': sum1 += 1
            except: next
            try:
                if text[i-1][j+1] == 'M' and text[i-2][j+2] == 'A' and text[i-3][j+3] == 'S': sum1 += 1
            except: next
            try:
                if text[i+1][j-1] == 'M' and text[i+2][j-2] == 'A' and text[i+3][j-3] == 'S': sum1 += 1
            except: next

        if text[i][j] == 'A':
            try:
                if text[i-1][j-1] == 'M' and text[i-1][j+1] == 'M' and text[i+1][j-1] == 'S' and text[i+1][j+1] == 'S': sum2 += 1
            except: next
            try:
                if text[i-1][j-1] == 'M' and text[i-1][j+1] == 'S' and text[i+1][j-1] == 'M' and text[i+1][j+1] == 'S': sum2 += 1
            except: next
            try:
                if text[i-1][j-1] == 'S' and text[i-1][j+1] == 'M' and text[i+1][j-1] == 'S' and text[i+1][j+1] == 'M': sum2 += 1
            except: next
            try:
                if text[i-1][j-1] == 'S' and text[i-1][j+1] == 'S' and text[i+1][j-1] == 'M' and text[i+1][j+1] == 'M': sum2 += 1
            except: next

print("La première réponse est", sum1)
print("La deuxième réponse est", sum2)