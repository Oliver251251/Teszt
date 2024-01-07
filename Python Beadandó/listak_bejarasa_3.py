szamok = [120, 9, 5, 24, 6, 17, -45, 92, 15, 48, 57]
print('3-al osztható páros számok:')
for item in szamok:
    if(item % 3 == 0 and item % 2 == 0):
        print(item)