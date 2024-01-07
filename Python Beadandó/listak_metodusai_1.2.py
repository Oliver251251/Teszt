szinek = ['piros', 'zöld', 'kék', 'piros']
tipp = input('Adjon meg egy színt: ')
if(tipp in szinek):
    print(f'A szín már szerepel a listában {szinek.count(tipp)} alkalommal')
else:
    print('A megadott szín még nem szerepel a listában')

print(f'Színek: {szinek}')