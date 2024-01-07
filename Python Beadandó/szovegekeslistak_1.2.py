mondat = input('Adj meg egy mondatot(fontos a mondatvégi írásjel):')
mondatok = list()

while(mondat != ''):
    mondatok.append(mondat)
    mondat = input('Adj meg egy mondatot(fontos a mondatvégi írásjel):')

for item in mondatok:
    if(item[len(item) - 1] == '.'):
        print(f'A következő mondat: "{item}", kijelentő mondat')
    elif(item[len(item) - 1] == '?'):
        print(f'A következő mondat: "{item}", kérdő mondat')
    elif(item[len(item) - 1] == '!'):
        print(f'A következő mondat: "{item}", felkiáltó/felszólító/óhajtó mondat')
    else:
        print('Nincs mondatvégi írásjel')