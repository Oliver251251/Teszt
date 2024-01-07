szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
lista = list()
for item in szavak:
    if(item.lower().startswith('t')):
        lista.append(item)

print(f'A "t" vagy "T"-vel kezdődő szavak: {lista}')