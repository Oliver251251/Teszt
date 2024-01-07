import random

szamlalo = 0
for i in range(20):
    rnd = random.randint(1,12)
    if(rnd % 3 == 0):
        szamlalo += 1
        print(rnd)


print(f"{szamlalo}db 3-al olsztható szám volt")