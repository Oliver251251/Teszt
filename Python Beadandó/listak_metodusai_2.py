import random

szamok = list()

for i in range(10):
    szamok.append(random.randint(1,3))
print(f'Számok: {szamok}')
eltavolit = int(input("Adj meg egy szémot amit eltávolítsunk: "))
print(f'Változtatott számok: {[i for i in szamok if i != eltavolit]}')