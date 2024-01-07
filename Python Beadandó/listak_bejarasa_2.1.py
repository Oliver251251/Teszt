szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
print('A "t" vagy "T"-vel kezdődő szavak:')
for item in szavak:
    if(item.lower().startswith('t')):
        print(item)