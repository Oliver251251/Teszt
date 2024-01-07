szinek = ['piros', 'zöld', 'kék']

if(input('Adjon meg egy színt: ') in szinek):
    print('A szín már szerepel a listában')
else:
    print('A szín még nem szerepel a listában')

print(f'Színek: {szinek}')