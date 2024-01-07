szoveg = input("Adj meg egy szöveget: ")
hanyszor = input("Hányszor írjam ki?: ")

while(hanyszor.isdigit() != True):
    hanyszor = input("Hányszor írjam ki?(számot adj meg): ")

for i in range(int(hanyszor)):
    print(szoveg)