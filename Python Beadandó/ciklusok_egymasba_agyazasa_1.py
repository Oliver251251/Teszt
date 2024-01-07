number = int(input("Kérlek adj meg egy páros számot: "))

if number % 2 != 0:
    print("A megadott szám nem páros!")
else:
    middle_row = number // 2

    for i in range(1, number + 1):
        if i <= middle_row:
            print("O " * i)
        else:
            print("O " * (number - i + 1))