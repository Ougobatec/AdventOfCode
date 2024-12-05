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
            with open(solution, 'w') as f: f.write(f"# Solution pour le jour {day:02d} de l'Advent of Code {year}\n")
            print(f"Le fichier {path}/solution a été créer.")
        
        if not os.path.exists(input):
            with open(input, 'w') as f: pass
            print(f"Le fichier {path}/solution a été créer.")