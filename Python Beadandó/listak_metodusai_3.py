betuk = list()

betu = input('Adjon meg egy betűt: ')

while(betu != ''):
    if((betu.lower() not in betuk) and (betu.upper() not in betuk)):
        betuk.append(betu)
    else:
        print('Ezt a betűt már rögzítettem.')

    uppercase = sorted([x for x in betuk if x.isupper()])
    lowercase = sorted([x for x in betuk if x.islower()])

    print(uppercase + lowercase)
    betu = input('Adjon meg egy betűt: ')