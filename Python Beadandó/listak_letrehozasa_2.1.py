lista = list()
beker = input('Adj meg egy "a" betűvel kezdődő szót: ')

while(beker != ''):
    if(not beker.startswith('a')):
        beker = input('A szó nem került mentésre mert nem kis "a"-val kezdődött. Adj meg egy "a" betűvel kezdődő szót: ')
    else:
        lista.append(beker)
        beker = input('Adj meg egy újjabb "a" betűvel kezdődő szót: ')

for item in lista:
    print(item)