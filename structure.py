import os
import datetime

now = datetime.datetime.now().year
years = list(range(2015, now+1))

for year in years:
    os.makedirs(str(year), exist_ok=True)
    
    for day in range(1, 26):
        path = f"{year}/{day:02d}"
        os.makedirs(path, exist_ok=True)
        
        solution = os.path.join(path, "solution.py")
        input = os.path.join(path, "input.txt")

        if not os.path.exists(solution):
            with open(solution, 'w', encoding='utf-8') as f:
                f.write(f'# Solution pour le jour {day:02d} de l\'Advent of Code {year}\n\n')
                f.write(f'# with open("./{year}/{day:02d}/input.txt") as f: lines = [line.strip() for line in f.readlines()]\n\n')
                f.write('# res1 = 0\n')
                f.write('# print("La première réponse est", res1)\n\n')
                f.write('# res2 = 0\n')
                f.write('# print("La deuxième réponse est", res2)')
            print(f"Le fichier {path}/solution a été créer.")
        
        if not os.path.exists(input):
            with open(input, 'w') as f: pass
            print(f"Le fichier {path}/solution a été créer.")