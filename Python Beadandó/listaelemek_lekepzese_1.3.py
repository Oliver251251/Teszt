szavak = ['alma', 'alom', 'malom', 'majom','bajom', 'fajom', 'bar', 'om']
print(f'Eredeti szavak: {szavak}')
nagyszavak = list()

for i in range(len(szavak)):
    if(len(szavak[i]) > 3):
        nagyszavak.append(szavak[i].upper())
print(f'Nagybetűvel: {nagyszavak}')