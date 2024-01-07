szamlalo = 0
for i  in range(0, 7):
    for j in range(0, 7):
        if(i == j or i + j == 6):
            print('O', end=' ')
        else:
            print('.', end=' ')
    print()