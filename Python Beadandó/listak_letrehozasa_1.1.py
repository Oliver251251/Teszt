nevek = list()
nev = input('Kérlek adj meg egy keresztnevet: ')
while(nev != ''):
    nevek.append(nev)
    nev = input('Kérlek adj meg egy keresztnevet: ')

for item in nevek:
    print(item)