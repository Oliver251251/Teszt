mondat = input('Adj meg egy mondatot(fontos a mondatvégi írásjel):')

if(mondat[len(mondat) - 1] == '.'):
    print('Kijelentő mondat')
elif(mondat[len(mondat) - 1] == '?'):
    print('Kérdő mondat')
elif(mondat[len(mondat) - 1] == '!'):
    print('Felkiáltó/felszólító/óhajtó mondat')
else:
    print('Nincs mondatvégi írásjel')