nevek = list()
nev = ' '
while(nev != '' and len(nevek) != 3):
    nev = input('Kérlek adj meg egy keresztnevet: ')
    nevek.append(nev)

    if(len(nevek) == 3):
        print('Nincs lehetősége újabb adat bevitelére!')

for item in nevek:
    print(item)