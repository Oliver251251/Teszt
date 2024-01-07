szavak = ['alma', 'alom', 'malom', 'majom','bajom', 'fajom']
nagyszavak = list()
print(f'Eredeti szavak: {szavak}')

for i in range(len(szavak)):
   nagyszavak.append(szavak[i].upper())
print(f'Nagybetűvel: {nagyszavak}')