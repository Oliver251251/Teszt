lista = list()
beker = input('Adj meg egy "a" vagy "A" betűvel kezdődő szót: ')

while(beker != ''):
    if(not beker.lower().startswith('a')):
        beker = input('A szó nem került mentésre mert "a" vagy "A"-val kezdődött. Adj meg egy "a" betűvel kezdődő szót: ')
    else:
        lista.append(beker)
        beker = input('Adj meg egy újjabb "a" vagy "A" betűvel kezdődő szót: ')

for item in lista:
    print(item)