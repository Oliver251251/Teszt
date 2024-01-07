szamlalo = 0
for i  in range(0, 5):
    for j in range(0, 5):
        if(i == j):
            print('O', end=' ')
        else:
            print('.', end=' ')
    print()