import random

szamok = list()

for i in range(10):
    szam = random.randint(0, 50)
    if(szam % 4 == 0):
        szamok.append(szam)

print(szamok)
print(f'A lista {len(szamok)} elemből áll')