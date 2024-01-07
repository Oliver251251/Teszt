szavak = ['alma', 'alom', 'malom', 'majom','bajom', 'fajom', 'bar', 'om']
print(f'Eredeti lista: {szavak}')
generalt = list()

for i in range(len(szavak)):
    generalt.append(szavak[i].title())
print(f'Nagybetűvel: {generalt}')